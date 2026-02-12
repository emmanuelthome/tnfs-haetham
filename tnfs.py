# from cube_enumerate import *
# from utils import indexed_set
import itertools
import functools
import sage.misc.banner

if sage.misc.banner.require_version(10, 1, 0):
    from sage.misc.timing import cputime
else:
    from sage.misc.misc import cputime
from sage.rings.rational_field import QQ
from sage.arith.misc import legendre_symbol, gcd, next_prime
from sage.arith.functions import lcm
from sage.rings.number_field.number_field import NumberField
from sage.rings.finite_rings.integer_mod_ring import ZZ, Integers
from sage.rings.finite_rings.finite_field_constructor import GF
from sage.rings.fast_arith import prime_range
from sage.misc.prandom import randint
from sage.misc.functional import log
from sage.matrix.special import block_matrix, block_diagonal_matrix
from sage.matrix.constructor import matrix
from sage.modules.free_module_element import vector
from collections import defaultdict
from sage.misc.prandom import randrange
from sage.categories.homset import Hom
from sage.rings.real_mpfr import RR
from time import time
from sage.misc.misc_c import prod
import cube_enumerate
import os
import math
from math import sqrt
import utils
import concurrent.futures
import copy
import sys
import pickle
import subprocess
from sage.arith.power import generic_power
from sage.arith.misc import divisors

# from fpylll import IntegerMatrix
# from fpylll.util import gaussian_heuristic
# try:
#     from g6k import Siever
# except ImportError:
#     raise ImportError("g6k not installed. Either install it yourself, or run caramba's sage-g6k")
# from simple_pump import pump


# from sage.misc.cython import cython_import, cython_import_all
# # utils = cython_import("utils.pyx")
# schnorr_euchner = cython_import("schnorr_euchner.pyx")
import schnorr_euchner


def _prime_is_ok_tnfs(p, h, f1, f2_splitter, dh, df):
    if not f2_splitter.roots(GF(p)):
        return False

    if [c.degree() for c, k in h.change_ring(GF(p)).factor()] != [dh]:
        return False

    # Pourquoi c'est pas [df, ... autre chose]?
    # if [c.degree() for c, k in f1.change_ring(GF(p)).factor()] != [df, df]:
    #    print(3)
    #    return False
    if not df in [c.degree() for c, _ in f1.change_ring(GF(p)).factor()]:
        return False

    ell, _ = f1.parent().cyclotomic_polynomial(dh * df)(p).factor()[-1]
    if gcd(ell, p - 1) != 1:
        return False

    assert ell % (dh * df) == 1

    return True


def _rational_reconstruction_insist(x):
    i = 0
    while True:
        i += 1
        try:
            uv = (i * x).rational_reconstruction()
        except ArithmeticError:
            continue
        uv /= i
        u = uv.numerator()
        v = uv.denominator()
        return u, v


def _largest_factor(fac):
    if len(fac) == 0:
        return 1
    else:
        return fac[-1][0]


def is_stable_orbit(sigma, L):
    return set([sigma(x) for x in L]) == set(L)


def get_orbits(sigma, order, ideals):
    orbits = []
    i = 0
    while i < len(ideals):
        j = 1
        while j <= order and i + j <= len(ideals):
            if is_stable_orbit(sigma, ideals[i : i + j]):
                break
            assert j < order
            j += 1
        orbits.append((i, i + j))
        i += j
    return orbits


def compressor_from_orbits(zeta, orbits, pw):
    n = orbits[-1][1]
    compressor = matrix(zeta.parent(), n, len(orbits))
    i = 0
    for k, j0j1 in enumerate(orbits):
        j0, j1 = j0j1
        span = j1 - j0
        xi = zeta**pw
        rho = 1
        for z in range(span):
            compressor[i, k] = rho
            rho *= xi
            i += 1
    return compressor


def poor_man_xgcd(A, B):
    """
    This is used for example with Polynomial_dense_modn_ntl_ZZ which does
    not provide xgcd
    See https://doc.sagemath.org/html/en/reference/polynomial_rings/sage/rings/polynomial/polynomial_modn_dense_ntl.html#sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_modn_ntl_ZZ
    """
    R = A.parent()
    m = matrix(R, 2, 2, [1, 0, 0, 1])
    a = A
    b = B
    while b != 0:
        q, r = a.quo_rem(b)
        m = matrix(2, 2, [0, 1, 1, -q]) * m
        a = b
        b = r
    u, v = m[0]
    return a, u, v


class NotSmooth(Exception):
    def __init__(self, phi, field_name):
        super().__init__(f"{phi} involves unmet ideals in {field_name}")


class relation_search(object):
    def __init__(self, TT):
        self.TT = TT
        self.set_phi = []
        self.ignore_phi = set()
        self.ignore_a_div_b = set()
        self.ignore_norm_pairs = set()
        self.primes1 = set()
        self.primes2 = set()
        self.aborts = [0] * 7
        # try:
        #     self.F = f"{{:{os.get_terminal_size().columns-2}s}}"
        # except OSError:
        #     self.F = "{:s}"
        self.F = "{:s}"
        self.st = 0
        self.st0 = -time()
        self.multithreaded = 0

    def __enter__(self):
        print("Looking for smooth a,b pairs")
        return self

    def __exit__(self, *args, **kwargs):
        self.st0 += time()
        print(self.F.format(f"Looking for smooth a,b pairs: done in {self.st0:.2f}"))

    def progress(self, aibi, x=""):
        print(self.F.format(f"{aibi} {self.aborts} {x}"), end="\r")

    def try_ab(
        self,
        a,
        b,
        smoothness_bound,
        factor_first=1,
        prescribed=[1, 1],
        kill_orbits=True,
        machine_output=False,
    ):
        phi = a - b * self.TT.KhP.gen()

        if a == 0 and b != 1 or a != 1 and b == 0:
            self.aborts[1] += 1
            return None

        if a and b:
            if a / b in self.ignore_a_div_b:
                self.aborts[2] += 1
                return None
            self.ignore_a_div_b.add(a / b)
        if kill_orbits:
            orbit = self.TT.conjugates_phi(phi)
            for c in orbit:
                if c.denominator()==1 and c.numerator().degree()==1: # if it is of the form a - b T
                    if c.numerator()[0] and c.numerator()[1]:
                        self.ignore_a_div_b.add(-c.numerator()[0] / c.numerator()[1])

        # np = (self.TT.quicknorm1(phi), self.TT.quicknorm2(phi))
        # if np in self.ignore_norm_pairs:
        #     self.aborts[3] += 1
        #     return None

        # This side is larger, we have better chance of discarding
        # the pair early on if we start with this one.
        for i in range(2):
            side = factor_first ^ i
            if side == 1:
                self.st -= cputime()
                np2 = self.TT.quicknorm2(phi)
                assert np2 % prescribed[1] == 0
                np2 = np2 // prescribed[1]
                fac2 = np2.factor()
                self.st += cputime()
                l2 = _largest_factor(fac2)
                if l2 >= smoothness_bound:
                    self.aborts[4] += 1
                    return None
            else:
                self.st -= cputime()
                np1 = self.TT.quicknorm1(phi)
                assert np1 % prescribed[0] == 0
                np1 = np1 // prescribed[0]
                fac1 = np1.factor()
                self.st += cputime()
                l1 = _largest_factor(fac1)
                if l1 >= smoothness_bound:
                    self.aborts[5] += 1
                    return None

        # Sage absurdity world here. It seems that it's faster to do
        # the gcd check now rather than before the factorizations!
        # The call to fractional_ideal with several elements entails
        # an HNF call. It should be quick, though.

        # FIXME: If OKh is not principal, we're forgetting people
        # here. a,b may share a common non-principal ideal
        # in common, yet there's no other way to reach that
        # factorization...
        # if self.TT.OKh.fractional_ideal(a, b) != 1:
        #     self.aborts[6] += 1
        #     return None
        #
        # perhaps something along the lines of killing based on
        # a/b ?

        # We have a relation !
        # self.ignore_norm_pairs.add(np)

        fac1 = list(fac1)
        fac2 = list(fac2)
        if prescribed[0] != 1:
            fac1.append((prescribed[0], 1))
        if prescribed[1] != 1:
            fac2.append((prescribed[1], 1))
        for p, c in sorted(fac1):
            self.primes1.add(p)
        for p, c in sorted(fac2):
            self.primes2.add(p)
        self.set_phi.append(phi)

        if not machine_output:
            print(
                self.F.format(
                    f"{self.st0+time():.2f} {self.st:.2f} {len(self.set_phi)} ({len(self.primes1)}, {len(self.primes2)}) {phi}"
                )
            )
        else:
            L = self.serialize_result_inner(
                [phi], [p for p, c in fac1], [p for p, c in fac2]
            )
            for x in L:
                print(x)

        return True

    def serialize_result_inner(self, set_phi, primes1, primes2):
        L = ["PHI", len(set_phi)]
        for phi in set_phi:
            la = list(phi[0])
            lb = list(-phi[1])
            L += [len(la)] + la
            L += [len(lb)] + lb
        L += ["PRIMES1", len(primes1)] + sorted(primes1)
        L += ["PRIMES2", len(primes2)] + sorted(primes2)
        return L

    def serialize_result(self):
        return self.serialize_result_inner(self.set_phi, self.primes1, self.primes2)

    def catch_result(self, taskname, iter):
        try:
            while True:
                while (u := next(iter).decode("utf-8").strip()) != "PHI":
                    print(taskname + ": " + u)
                latest = []
                for i in range(int(next(iter))):
                    a = [ZZ(next(iter)) for j in range(int(next(iter)))]
                    b = [ZZ(next(iter)) for j in range(int(next(iter)))]
                    phi = self.TT.Kh(a) - self.TT.Kh(b) * self.TT.KhP.gen()
                    latest.append(phi)
                    self.set_phi.append(phi)
                assert next(iter).decode("utf-8").strip() == "PRIMES1"
                for p in [ZZ(next(iter)) for i in range(int(next(iter)))]:
                    self.primes1.add(p)
                assert next(iter).decode("utf-8").strip() == "PRIMES2"
                for p in [ZZ(next(iter)) for i in range(int(next(iter)))]:
                    self.primes2.add(p)
                for phi in latest:
                    print(
                        self.F.format(
                            f"{self.st0+time():.2f} {self.st:.2f} {len(self.set_phi)} ({len(self.primes1)}, {len(self.primes2)}) {phi}"
                        )
                    )
        except StopIteration:
            pass

        print(f"Done collecting results from {taskname}")

    def exhaustive_search(self, *args, **kwargs):
        E = (
            kwargs.get("El", 0)
            or kwargs.get("exploration_bound", 0)
            or kwargs.get("E", 0)
        )
        S = kwargs.get("smoothness_bound", 0) or kwargs.get("S", 0)
        # cube_enumerate can't work from cython, but from python it's ok.
        # for aibi in itertools.product(
        #     range(-exploration_bound, exploration_bound + 1),
        #     repeat=2*self.h.degree()
        # ):
        logA = 2 * self.TT.h.degree() * log(2 * E + 1) / log(2) - 1
        print("Search space size: A={:.1f} bits".format(float(logA)))
        nb_elements = 100
        norm1_avg = log(
            sum(
                [
                    float(self.TT.quicknorm1(self.TT.get_phi(E)))
                    for i in range(nb_elements)
                ]
            )
            / float(nb_elements),
            2,
        )
        norm2_avg = log(
            sum(
                [
                    float(self.TT.quicknorm2(self.TT.get_phi(E)))
                    for i in range(nb_elements)
                ]
            )
            / float(nb_elements),
            2,
        )
        print(
            "Norm bits in [-{},{}]^{}: ({:.2f}, {:.2f})".format(
                E, E, 2 * self.TT.h.degree(), float(norm1_avg), float(norm2_avg)
            )
        )
        # for exhaustive search on baby examples like this,
        # and somewhat counter-intuitively, we factor the small norm
        # first, because otherwise the arithmetic cost is large.
        factor_first = 0 if norm1_avg < norm2_avg else 1
        self.kill_orbits = True
        for aibi in cube_enumerate.cube_enumerate(2 * self.TT.h.degree(), E):
            a = self.TT.Kh(aibi[: self.TT.h.degree()])
            b = self.TT.Kh(aibi[self.TT.h.degree() :])
            if a[0] > 0:
                self.aborts[0] += 1
                continue
            self.try_ab(a, b, S, factor_first)
            ## self.progress(aibi)

    def special_q_sieving_prepare(self, E):
        # Form a list of q's. We want to find out where the norm is
        # large.
        nb_elements = 1000
        norm1_avg = log(
            sum(
                [
                    float(self.TT.quicknorm1(self.TT.get_phi(E)))
                    for i in range(nb_elements)
                ]
            )
            / float(nb_elements),
            2,
        )
        norm2_avg = log(
            sum(
                [
                    float(self.TT.quicknorm2(self.TT.get_phi(E)))
                    for i in range(nb_elements)
                ]
            )
            / float(nb_elements),
            2,
        )
        print(
            "Norm bits in [-{},{}]^{}: ({:.2f}, {:.2f})".format(
                E, E, 2 * self.TT.h.degree(), float(norm1_avg), float(norm2_avg)
            )
        )
        # 0 for f1, 1 for f2.
        sqside = 1 if norm2_avg > norm1_avg else 0
        assert self.TT.h.leading_coefficient() == 1
        iota = self.TT.Kh.gen()
        assert self.TT.OKh.basis() == [iota**i for i in range(self.TT.h.degree())]
        print("Special-q on {} side".format("f2" if sqside else "f1"))
        return sqside

    def special_q_sieving_qlist(self, sqside, q0, q1, smoothness_bound):
        # print("Creating q-list")
        # st = -cputime()
        OO = [self.TT.OK1, self.TT.OK2]
        O = OO[sqside]
        disc = O.absolute_discriminant()
        K = O.number_field()
        f = K.defining_polynomial()
        h = self.TT.h

        for q in prime_range(q0, q1):
            if disc % q == 0:
                continue
            met = set()
            for rh, m in h.roots(GF(q)):
                if m > 1:
                    continue
                for rf, m in f.roots(GF(q)):
                    if m > 1:
                        continue
                    if (rh, rf) in met: 
                        continue
                    rrh, rrf = rh, rf
                    for i in range(self.TT.n):
                        if (rrh, rrf) in met:
                            break
                        met.add((rrh, rrf))
                        rrh = self.TT.tau(rrh)
                        rrf = self.TT.rho(rrf)
                    yield sqside, q, rh, rf # Only consider one-special-q per orbit

    def qr_to_ideal(self, sqside, q, rh, rf):
        OO = [self.TT.OK1, self.TT.OK2]
        O = OO[sqside]
        disc = O.absolute_discriminant()
        h = self.TT.h
        dh = h.degree()
        iota = self.TT.Kh.gen()
        alpha = O.number_field().gen()
        Lq = matrix(ZZ, dh * 2, dh * 2)
        Lq[0, 0] = q
        for i in range(1, dh):
            Lq[i, i - 1] = -ZZ(rh)
            Lq[i, i] = 1
        for i in range(dh):
            Lq[i + dh, i] = ZZ(rf)
            Lq[i + dh, i + dh] = 1
        elems = [q, iota - ZZ(rh), alpha - ZZ(rf)]
        I = O.fractional_ideal(*elems).numerator()
        assert I.is_prime()
        assert I.absolute_norm() == q
        # recompute the number of conjugates just for fun.
        met = set()
        rrh, rrf = rh, rf
        for i in range(self.TT.n):
            if (rrh, rrf) in met:
                break
            met.add((rrh, rrf))
            rrh = self.TT.tau(rrh)
            rrf = self.TT.rho(rrf)

        return f"({q},iota-{rh},{alpha}-{rf}; {len(met)} conjugates)", I, Lq

        #    for I,m in OO[sqside].fractional_ideal(q).factor():
        #        if I.absolute_norm() == q:
        #            # qlist.append(I)
        #            yield I
        # st += cputime()
        # print(f"Creating q-list ({len(qlist)} ideals): done in {st:.2f}s")

    def special_q_sieving(self, *args, **kwargs):
        # We want to explore in a ball of radius exploration_bound, so
        # with squared norm <= n*exploration_bound^2

        n = self.TT.n
        n_tau = self.TT.n_tau
        E = (
            kwargs.get("Eq", 0)
            or kwargs.get("exploration_bound", 0)
            or kwargs.get("E", 0)
        )
        S = kwargs.get("smoothness_bound", 0) or kwargs.get("S", 0)
        q0 = kwargs.get("q0", None)
        q1 = kwargs.get("q1", None)
        if q0 is None:
            q0 = S // 2
        if q1 is None:
            q1 = 3 * S // 2
        # radius = sqrt(2*n_tau) * E
        # pick a radius so that we have roughly the same number of
        # in the orthotope and in the total of all the q-lattices.
        #
        # If we have a volume C*E^(2n_tau) in the ball, each q-lattice has
        # C*E^(2n_tau)/q points in there, so that we eventually get
        # \sum_{q=q_0}^{q_1} C\cdot \frac{E^(2n_tau)}{nq\log q}
        # = C \cdot E^(2n_tau)/n \left(\log\log q_1 - \log\log q_0)
        #
        # (The division by n comes from the automorphisms)

        ortho_logA = float(2 * n_tau * log(2 * E + 1) / log(2)) - 1
        print("Size of [-{},{}]^{}: {:.2f} bits".format(E, E, 2 * n_tau, ortho_logA))

        logvol = lambda n, R: n * (log(RR.pi()) / 2 + log(R)) - math.lgamma(n / 2 + 1)

        # first get Ex such that ball(Ex, n) and ortho(E, n) have roughly
        # the same number of points.
        Ex = (2 * E + 1) / sqrt(RR.pi()) * math.gamma(n_tau + 1) ** (1 / 2 / n_tau)
        # These two are equal
        # print(2 * n_tau * log(2*E+1))
        # print(logvol(2 * n_tau, Ex))

        # if we multiply the radius by M, the total size across all q's
        # becomes ((loglog(q1)-loglog(q0))/n)*M^(2n_tau)

        radius = float(Ex * (log(log(q1) / log(q0)) / n) ** (-1.0 / (2 * n_tau)))

        logA0 = logvol(2 * n_tau, radius) / log(2) - 1

        # This should be about the same as ortho_logA...
        logA = logA0 + log(log(log(q1) / log(q0)) / n) / log(2)

        print("Search space size (per q): {:.1f} bits".format(float(logA0)))
        print("Search space size (all qs): A={:.1f} bits".format(float(logA)))
        print(
            "Expected number of lattice points per q: {:.1f} down to {:.1f}".format(
                math.floor(2**logA0 / q0), math.floor(2**logA0 / q1)
            )
        )

        sqside = self.special_q_sieving_prepare(E)

        # this is just an iterable.
        tasks = self.special_q_sieving_qlist(sqside, q0, q1, S)

        if self.multithreaded <= 1:
            for t in tasks:
                self.sieve_one_q(*t, radius, S)
        else:

            def reenter(R, name, *args):
                cmd = [
                    "sage",
                    "tnfs-client.sage",
                    R.TT._serialize(),
                    "sieve-one-special-q",
                ] + [str(x) for x in args]
                cmd = " ".join(cmd)
                print(cmd)
                cmd = cmd.split()
                with subprocess.Popen(
                    cmd, bufsize=0, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE
                ) as T:
                    # Because we have the GIL here, this safely appends
                    # to the global stuff, I think
                    R.catch_result(name, T.stdout)

            with concurrent.futures.ThreadPoolExecutor(
                max_workers=self.multithreaded
            ) as executor:
                thread_pool = []
                for t in tasks:
                    name = "{},q={},rh={},rf={}".format(*t)
                    T = executor.submit(reenter, self, name, *t, radius, S)
                    thread_pool.append(T)
                for T in thread_pool:
                    T.result()
        print("")

    def sieve_one_q(
        self, sqside, q, rh, rf, radius, smoothness_bound, machine_output=False
    ):
        dq, Iq, Lq = self.qr_to_ideal(sqside, q, rh, rf)
        prescribed = [1, 1]
        K = Iq.number_field()
        f = K.defining_polynomial()
        lc = f.leading_coefficient()
        q = Lq.determinant()
        prescribed[sqside] = q
        S = schnorr_euchner.SchnorrEuchnerEnumeration(Lq, radius)
        gamma1 = float(S.LM[0].norm())
        print(
            self.F.format(f"Now sieving {dq}, radius={radius:.2f}, gamma1={gamma1:.2f}")
        )
        lattice_points = S.enum()
        try:
            print(self.F.format(f"Lattice points: {len(lattice_points)}"))
        except TypeError:
            print(self.F.format(f"Lattice points: using online enumeration"))
        for aibi in S.enum():
            a = self.TT.Kh(aibi[: self.TT.h.degree()])
            b = self.TT.Kh(aibi[self.TT.h.degree() :])
            if b:
                assert (a - b * K.gen()) * lc in Iq
            self.try_ab(
                a,
                b,
                smoothness_bound,
                1 - sqside,
                prescribed,
                kill_orbits=False,
                machine_output=machine_output,
            )
            ## self.progress(aibi)


class tnfs(object):
    def __set_universal_constants__(self):
        self.ZP = ZZ["x"]
        self.ZPP = self.ZP["T"]

    def __set_from_family(self, family):
        x = self.ZP.gen()
        T = self.ZPP.gen()
        f2 = None
        if family == "example4":
            h = x**3 + x + 1
            Kh = NumberField(h, "iota")
            iota = Kh.gen()
            f2_family = (iota + 2) * x**2 + 3 * T * x + iota + 2
            f2_splitter = T**2 + iota * T + 1
            f1 = f2_family.resultant(f2_splitter)
            tau = lambda iota: 1 / iota
            rho = lambda alpha: 1 / alpha
            n_tau = 2
            n_rho = 2
            n = 4
            p = 83

        elif family == "example6":
            h = x**3 - x**2 - 2 * x + 1
            f2_family = x**2 - T * x + 1
            f2_splitter = T**2 - 2
            f1 = f2_family.resultant(f2_splitter)
            tau = lambda iota: 1 / (1 - iota)
            rho = lambda alpha: 1 / alpha
            n_tau = 3
            n_rho = 2
            n = 6
            p = -50
        elif family == "example6b":
            h = x**3 - x**2 - 2 * x + 1
            f2_family = x**2 - T * x + 1
            f2_splitter = T**2 + 1
            f1 = f2_family.resultant(f2_splitter)
            tau = lambda iota: 1 / (1 - iota)
            rho = lambda alpha: 1 / alpha
            n_tau = 3
            n_rho = 2
            n = 6
            p = -50
        elif family == "example6c":  # we define f2
            h = x**3 - x**2 - 2 * x + 1
            f1 = x**4 + 3 * x**2 + 1
            f2 = -2 * x**2 + 5
            tau = lambda iota: 1 / (1 - iota)
            rho = lambda alpha: -alpha
            n_tau = 3
            n_rho = 2
            n = 6
            p = -50
        elif family == "example6d":  # create even polynomials
            h = x**3 - x**2 - 2 * x + 1
            f2_family = x**2 + T + 22
            f2_splitter = T**2 - 2
            f1 = f2_family.resultant(f2_splitter)
            tau = lambda iota: 1 / (1 - iota)
            rho = lambda alpha: -alpha
            n_tau = 3
            n_rho = 2
            n = 6
            p = -50
        elif family == "example6e":  # eta=2
            h = x**2 + x + 1
            f2_family = x**3 - T*x**2 -(T+3)*x - 1 
            f2_splitter = T**2 + 1
            f1 = f2_family.resultant(f2_splitter)
            tau = lambda iota: 1 / iota
            rho = lambda alpha: - (alpha+1)/alpha
            n_tau = 2
            n_rho = 3
            n = 6
            p = -50 
        elif family == "example6_disc_f2_pos":
            h = x**3 - x**2 - 2 * x + 1
            f2_family = x**2 - 4 * T * x + 1
            f2_splitter = T**2 - 2
            f1 = f2_family.resultant(f2_splitter)
            tau = lambda iota: 1 / (1 - iota)
            rho = lambda alpha: 1 / alpha
            n_tau = 3
            n_rho = 2
            n = 6
            p = -50
        elif family == "example12":
            h = x**4 - x**3 + x**2 - x + 1
            f2_family = x**3 - T * x**2 - (T + 3) * x - 1
            f2_splitter = T**2 + 1
            f1 = f2_family.resultant(f2_splitter)
            tau = lambda iota: iota**3
            rho = lambda alpha: -(alpha + 1) / alpha
            n_tau = 4
            n_rho = 3
            n = 12
            p = -50

        elif family == "example12b":
            h = x**4 + 4 * x**2 + 2
            f2_family = x**3 - T * x**2 - (T + 3) * x - 1
            f2_splitter = T**2 + 1
            f1 = f2_family.resultant(f2_splitter)
            tau = lambda iota: iota**3 + 3 * iota
            rho = lambda alpha: -(alpha + 1) / alpha
            n_tau = 4
            n_rho = 3
            n = 12
            p = -50
        
        elif family == "example12c":
            h = x**4 - x**3 + x**2 - x + 1
            f2_family = x**3 - T * x**2 - (T + 3) * x - 1
            f2_splitter = T**2 + 4
            f1 = f2_family.resultant(f2_splitter)
            tau = lambda iota: iota**3
            rho = lambda alpha: -(alpha + 1) / alpha
            n_tau = 4
            n_rho = 3
            n = 12
            p = -50

        elif family == "example12d": # eta = 3
            h = x**3 - x**2 - 2 * x + 1
            f2_family = x**4 +T*x**3 - 6*x**2 - T*x + 1
            f2_splitter = T**2 - 3
            f1 = f2_family.resultant(f2_splitter)
            tau = lambda iota: 1 / (1 - iota)
            rho = lambda alpha: -(alpha + 1) / (alpha-1)
            n_tau = 3
            n_rho = 4
            n = 12
            p = -50

        elif family == "example10":
            h = (
                x**5 - 2 * x**4 - 5 * x**3 + 2 * x**2 + 4 * x + 1
            )  # this is galois and has an automorphism of order 5
            f2_family = x**2 - T * x + 1
            f2_splitter = T**2 + 1
            f1 = f2_family.resultant(f2_splitter)
            tau = (
                lambda iota: -4 * iota**4 + 10 * iota**3 + 15 * iota**2 - 16 * iota - 8
            )
            rho = lambda alpha: 1 / alpha
            n_tau = 5
            n_rho = 2
            n = 10
            p = -50

        elif family == "example10b":
            h = (
                x**5 - x**4 - 4 * x**3 + 3 * x**2 + 3 * x - 1
            )  # this is galois and has an automorphism of order 5 : sigma : iota |--> -iota**2+2
            f2_family = x**2 + T * x + 1
            f2_splitter = T**2 + T + 1
            f1 = f2_family.resultant(f2_splitter)
            tau = lambda iota: -(iota**2) + 2
            rho = lambda alpha: 1 / alpha
            n_tau = 5
            n_rho = 2
            n = 10
            p = 7

        else:
            raise RuntimeError(f"Family '{family}' not supported")
        if f2 is None:
            assert f2_family.subs(x=rho(x)).numerator().gcd(f2_family) != 1
        assert h(tau(x)).numerator().gcd(h).degree() == h.degree()

        self.family = family
        self.h = h
        self.f1 = f1
        self.n = n
        self.n_tau = n_tau
        self.n_rho = n_rho
        self.tau = tau
        self.rho = rho

        # we have a few situations where these things are really expected
        assert self.n == self.n_tau * self.n_rho
        assert self.h.degree() == self.n_tau
        assert self.f1.degree() == self.n_rho * 2
        if f2 is None:
            assert f2_family(0).degree() == self.n_rho
        else:
            f2_family, f2_splitter = None, None
        return (p, f2_family, f2_splitter, f2)

    def __polyselect__(self, family=None, p=None, f2=None, ell=None, *args, **kwargs):
        p_default, f2_family, f2_splitter, f2 = self.__set_from_family(family)
        n = self.n

        if f2 is None:
            if p is None:
                p = p_default
            if p < 0:
                p = -p
                p = next_prime(p)
                while not _prime_is_ok_tnfs(
                    p, self.h, self.f1, f2_splitter, self.n_tau, self.n_rho
                ):
                    print(f"p={p} does not work, trying next prime")
                    p = next_prime(p)
                print(f"p={p} works")

            assert _prime_is_ok_tnfs(
                p, self.h, self.f1, f2_splitter, self.n_tau, self.n_rho
            )
            if ell is None:
                ell, _ = self.ZP.cyclotomic_polynomial(n)(p).factor()[-1]
                print(f"ell={ell}")
            # Now construct f2 with the conjugation method
            u, v = _rational_reconstruction_insist(f2_splitter.roots(GF(p))[0][0])
            assert f2_family.degree() == 1
            f2 = f2_family(u / v) * v
        else:
            # re-cast to ZP, so that we can easily accept lists.
            f2 = self.ZP(f2)
            assert p is not None
            if ell is None:
                ell, _ = self.ZP.cyclotomic_polynomial(n)(p).factor()[-1]
                print(f"ell={ell}")

        assert f2.change_ring(GF(p**(self.h.degree()))).is_irreducible()
        self.f2 = f2
        self.p = p
        self.ell = ell

        assert self.ZP.cyclotomic_polynomial(n)(p) % self.ell == 0
        assert gcd((p**n - 1) // ell, ell) == 1
        assert self.f1.resultant(self.f2) % self.p**self.n_rho == 0

    def __number_fields__(self):
        Kh = NumberField(self.h, "iota")
        KhP = Kh["T"]

        K1 = NumberField(KhP(self.f1), "alpha")
        K2 = NumberField(KhP(self.f2), "beta")

        # We don't need the absolute fields that much, except for checking
        K1a = K1.absolute_field("AAA")
        K2a = K2.absolute_field("BBB")

        OKh = Kh.maximal_order()
        OK1 = K1.maximal_order()
        OK2 = K2.maximal_order()
        OK1a = K1a.maximal_order()
        OK2a = K2a.maximal_order()

        self.Kh = Kh
        self.KhP = KhP
        self.K1 = K1
        self.K2 = K2
        self.K1a = K1a
        self.K2a = K2a
        self.OK1a = OK1a
        self.OK2a = OK2a
        self.OKh = OKh
        self.OK1 = OK1
        self.OK2 = OK2

    def __field_automorphisms__(self):
        # sigma is really the composition of rho and tau, and since these
        # two commute and have coprime degrees, the degree of sigma is
        # n==n_tau*n_rho
        Kh = self.Kh
        K1 = self.K1
        K2 = self.K2
        self.sigma_h = Hom(Kh, Kh)([self.tau(Kh.gen())])
        self.sigma_K1 = Hom(K1, K1)([self.rho(K1.gen())], base_map=self.sigma_h)
        self.sigma_K2 = Hom(K2, K2)([self.rho(K2.gen())], base_map=self.sigma_h)

    def __finite_fields__(self):
        ## descending from number fields to finite fields is a royal pain.
        p = self.p
        n = self.n
        ell = self.ell

        self.Fpn = GF(p**n)
        self.iota_p = self.h.change_ring(self.Fpn).roots()[0][0]
        self.z = self.f2.change_ring(self.Fpn).roots()[0][0]

        assert self.ZP.cyclotomic_polynomial(n)(p) % ell == 0
        self.cofac = (p**n - 1) // ell
        assert gcd(self.cofac, ell) == 1

        for i in range(p):
            self.logbase = self.Fpn.gen() + i
            if self.logbase**self.cofac != 1:
                return
        raise RuntimeError("Cannot find a generator of GF(p^n)^*")

    def __init__(self, *args, **kwargs):
        self.__set_universal_constants__()
        self.__polyselect__(*args, **kwargs)
        self.__number_fields__()
        self.__field_automorphisms__()
        self.__finite_fields__()
        self.__sm_setup__()
        # prepare empty lists so that we can do relation collection in
        # multiple calls
        self.set_ideals_K1 = utils.indexed_set()
        self.set_ideals_K2 = utils.indexed_set()
        self.stable_ideals_K1 = []
        self.stable_ideals_K2 = []
        self.list_phi = []

    """
    We can serialize/unserialize a tnfs object in two ways.

    First, to bytes. To do so, here is an example:
    
    sage: import tnfs
    sage: import io
    sage: TT = tnfs.tnfs('example12', p=-200)
	sage: foo = io.BytesIO()
	sage: tnfs.tnfs.Pickler(foo).dump(TT)
	sage: bar=io.BytesIO(foo.getvalue())
	sage: UU=tnfs.tnfs.Unpickler(bar).load()
    sage: assert TT.logbase == UU.logbase
    sage: assert TT.f2 == UU.f2
    """

    class Pickler(pickle.Pickler):
        def __init__(self, file, *args, **kwargs):
            super().__init__(file, *args, **kwargs)

        def dump(self, obj):
            assert isinstance(obj, tnfs)
            super().dump([obj.family, obj.p, obj.f2, obj.ell])

    class Unpickler(pickle.Unpickler):
        def __init__(self, file, *args, **kwargs):
            super().__init__(file, *args, **kwargs)

        def load(self):
            return tnfs(*super().load())

    """
    The second way to serialize is to a string

    sage: import tnfs
    sage: import io
    sage: TT = tnfs.tnfs('example12', p=-200)
	sage: blob = TT._serialize()
	sage: UU, tail =tnfs.tnfs._unserialize(blob)
    sage: assert TT.logbase == UU.logbase
    sage: assert TT.f2 == UU.f2

    """

    def _serialize(self):
        L = [str(x) for x in [self.family, self.p, self.f2.degree()]]
        L += [str(x) for x in list(self.f2)]
        L += [str(x) for x in [self.ell]]
        return " ".join(L)

    def _unserialize(*args):
        if len(args) == 1:
            data = iter(args[0].split())
        else:
            data = iter(args)
        family = next(data)
        p = ZZ(next(data))
        d = int(next(data))
        f2 = []
        for i in range(d + 1):
            f2.append(ZZ(next(data)))
        ell = ZZ(next(data))
        return tnfs(family, p, f2, ell), data

    def _K12_to_Fpn(self, e):
        # We would love to make that a morphism, but it can't work since it
        # is not defined for all rationals (p hurts...).
        # Kh._is_valid_homomorphism_(Fp3, [iota_p])
        #
        # and Kh.quotient_ring(p) does not work satisfactorily either,
        # because although it does define a coercion map, the codomain isn't
        # identified as being a finite field.
        P = [GF(self.p)["i"](list(c))(self.iota_p) for c in list(e)]
        s = P[-1]
        for i in range(1, len(P)):
            s = self.z * s + P[-1 - i]
        return s

    # funny enough, all three maps are the same.
    def K1_to_Fpn(self, e):
        return self._K12_to_Fpn(self.K1(e))

    def K2_to_Fpn(self, e):
        return self._K12_to_Fpn(self.K2(e))

    def KhP_to_Fpn(self, e):
        return self._K12_to_Fpn(self.KhP(e.numerator()))/self._K12_to_Fpn(self.KhP(e.denominator()))

    ## used for testing
    def get_phi(self, rbound):
        phi = self.KhP(0)
        iota = self.Kh.gen()
        T = self.KhP.gen()
        bound = math.floor(rbound)
        while True:
            a = self.ZP([randint(-bound, bound) for i in range(self.h.degree())])
            b = self.ZP([randint(-bound, bound) for i in range(self.h.degree())])
            if b == 0:
                continue
            if gcd(a.content(), b.content()) != 1:
                continue
            b *= b.leading_coefficient().sign()
            return a(iota) - b(iota) * T

    def quicknorm1(self, phi):
        return abs(phi.resultant(self.KhP(self.f1)).polynomial().resultant(self.h))

    def quicknorm2(self, phi):
        return abs(phi.resultant(self.KhP(self.f2)).polynomial().resultant(self.h))

    def quick_test_norms(self):
        ## just a test
        phi = self.get_phi(10)
        assert (
            self.quicknorm1(phi) / self.f1.leading_coefficient() ** self.h.degree()
            == phi(self.K1.gen()).absolute_norm()
        )
        assert (
            self.quicknorm2(phi) / self.f2.leading_coefficient() ** self.h.degree()
            == phi(self.K2.gen()).absolute_norm()
        )

    def _decompose_primes(self, O, sigma, primes, set_ideals, stable_ideals):
        for p in sorted(primes):
            D = set([I for I, k in O.fractional_ideal(p).factor()])
            while D:
                # pick an ideal at random, transform it by the
                # automorphisms we want to use, and register all these
                # ideals.
                # Note that it is super important that we add the ideals
                # in the order they are found by iterating sigma, because
                # the rest of the code expects it!
                I0 = D.pop()
                I = I0
                one_orbit = utils.indexed_set()
                while True:
                    one_orbit.add(I)
                    I = O.fractional_ideal(sigma(I))
                    if I == I0:
                        break
                    assert I in D
                    D.remove(I)
                if len(one_orbit) == self.n:
                    for I in one_orbit:
                        set_ideals.add(I)
                else:
                    for I in one_orbit:
                        stable_ideals.append(I)

        return set_ideals, stable_ideals

    def _relation_collection_get_phis(self, *args, **kwargs):
        """
        This is the first (and most expensive) step of the relation
        collection. We systematically explore all polynomials phi, and
        look out for the smooth ones. Smoothness is tested based on the
        resultants only, so it's all about factoring integers in the end.

        The list of phi is returned, together with the list of met primes
        on each side
        """
        with relation_search(self) as R:
            R.multithreaded = kwargs.get("multithreaded", 0)
            R.special_q_sieving(**kwargs)
            R.exhaustive_search(**kwargs)

            return R.set_phi, R.primes1, R.primes2

    # def sigma_KhP(self, phi):
    #     """
    #     Compute a function (polynomial over Kh) that gives the same quick
    #     norm, and has conjugate ideal factorization.

    #     This is harder than it seems. The problem is that we want to
    #     transform a polynomial (over Kh) to a polynomial. But we may very
    #     well encounter denominators when we apply rho. In fact, we most
    #     probably will, whether rho(alpha) is 1/alpha or some order-three
    #     automorphism.

    #     I'm not totally sure of what I'm doing ! It seems that it's hard
    #     to make sense out of this in a way that is consistent with all
    #     the cases I encounter.
    #     """

    #     T = self.KhP.gen()
    #     v = phi.valuation()
    #     # d = phi.degree()
    #     d = 1
    #     s = self.sigma_h
    #     rT = self.rho(self.KhP.gen())
    #     nn = rT.numerator()
    #     dd = rT.denominator()
    #     return sum([s(phi[i]) * nn ** (i) * dd ** (d - i) for i in range(v, d + 1)])
    
    def sigma_KhP(self, phi):
        """
        Compute a function (polynomial over Kh) that gives the same quick
        norm, and has conjugate ideal factorization.

        This is harder than it seems. The problem is that we want to
        transform a polynomial (over Kh) to a polynomial. But we may very
        well encounter denominators when we apply rho. In fact, we most
        probably will, whether rho(alpha) is 1/alpha or some order-three
        automorphism.

        I'm not totally sure of what I'm doing ! It seems that it's hard
        to make sense out of this in a way that is consistent with all
        the cases I encounter.

        TODO: The above function does not always work.
        Counter example :
        f1 = x^8 - 15*x^6 + 44*x^4 - 15*x^2 + 1
        with automorphism alpha : - (alpha+1)/(alpha-1)
        Applying the above function on phi = -T we get T+1 while we should get (T+1)/(T-1)
    
        """
        KhP = self.KhP
        T = KhP.gen()
        rT = self.rho(KhP.gen())
        nn = phi.numerator()
        nn = KhP(nn) # to apply degree even if integer or in Kh
        dd = phi.denominator()
        dd = KhP(dd)
        nn_conj = sum([self.sigma_h(nn[i]) * rT ** (i) for i in range(nn.degree()+1)])
        dd_conj = sum([self.sigma_h(dd[i]) * rT ** (i) for i in range(dd.degree()+1)]) 
        return nn_conj/dd_conj

    def conjugates_phi(self, phi):
        # TODO what is the proper conjugate of T ? It can't be 1...
        # somehow, I think that T must be considered stable, although I
        # don't find an easy way to grok that.
        #
        # (it's not that much of an issue, though)
        T = self.KhP.gen()
        assert phi.degree() <= 1
        a = phi[0]
        b = -phi[1]
        assert phi == a - b * T

        S = set()
        C = []
        for i in range(self.n):
            if phi in S:
                continue
            S.add(phi)
            C.append(phi)
            phi = self.sigma_KhP(phi)
        # We should really land on our feet.
        try:
            assert phi == a - b * T
        except AssertionError as e:
            print(f"Error for phi={a-b*T}")
            raise e
        return C

    def _create_ideals_set(self, primes1, primes2):
        print("Decomposing primes")
        st = -cputime()
        self._decompose_primes(
            self.OK1, self.sigma_K1, primes1, self.set_ideals_K1, self.stable_ideals_K1
        )
        self._decompose_primes(
            self.OK2, self.sigma_K2, primes2, self.set_ideals_K2, self.stable_ideals_K2
        )
        st += cputime()
        print(f"Decomposing primes: done in {st:.2f}")

    def _factor_one_phi(self, phi, stable_ideals=False):
        """
        if stable_ideals is true, also return (as a separate returned
        tuple) the ideals that are known to be invariant under a
        non-trivial subgroup of our explicit automorphism group. A
        priori, it should be OK to ignore these.
        """
        OK1 = self.OK1
        alpha = self.K1.gen()
        fac1 = []
        sfac1 = []
        for I, k in OK1.fractional_ideal(phi(alpha)).factor():
            try:
                j = self.set_ideals_K1.index(I)
                fac1.append((j, k))
            except KeyError:
                if stable_ideals:
                    j = self.stable_ideals_K1.index(I)
                    sfac1.append((j, k))

        OK2 = self.OK2
        beta = self.K2.gen()
        fac2 = []
        sfac2 = []
        for I, k in OK2.fractional_ideal(phi(beta)).factor():
            try:
                j = self.set_ideals_K2.index(I)
                fac2.append((j, k))
            except KeyError:
                if stable_ideals:
                    j = self.stable_ideals_K2.index(I)
                    sfac2.append((j, k))

        # It's a bit of a bummer. We want to make this an
        # immutable type so that we can make a set on it.
        fac12 = (tuple(sorted(fac1)), tuple(sorted(fac2)))

        if not stable_ideals:
            return fac12
        else:
            sfac12 = (tuple(sorted(sfac1)), tuple(sorted(sfac2)))
            return fac12, sfac12

    def relation_collection(self, *args, **kwargs):
        T = self.KhP.gen()
        alpha = self.K1.gen()
        beta = self.K2.gen()

        # Now we want to form relations involving ideals
        set_phi, primes1, primes2 = self._relation_collection_get_phis(**kwargs)

        self._create_ideals_set(primes1, primes2)

        print("Factoring into ideals")
        set_rows = utils.indexed_set()
        list_phi = []
        st = -cputime()
        for phi in set_phi:
            fac12 = self._factor_one_phi(phi)
            if fac12 in set_rows:
                continue
            if fac12 == ((), ()):
                continue
            set_rows.add(fac12)
            self.list_phi.append((phi, fac12))
            print(f"{st+cputime():.2f} {len(self.list_phi)} {phi}")
        st += cputime()
        print(f"Factoring into ideals: done in {st:.2f}")

    def expand_list_phi(self):
        self.list_phi = sum(
            [
                [(phi, self._factor_one_phi(phi)) for phi in self.conjugates_phi(phi)]
                for phi, fac12 in self.list_phi
            ],
            [],
        )

    @functools.cache
    def __SM1x_setup(self):
        self.SM1x_data = self.__SMx_setup(self.OK1, self.OK1a)
        # It's not a real technical obstacle, of course, but here
        # we're in the Galois case and we're super lazy, so let's
        # assume that everything is easy
        for I in self.SM1x_data[1]:
            assert self.expo1 == self.ell ** (I.residue_class_degree()) - 1
        # we always need at least one lift because we use it for the
        # computations of SMs once we're done with the reduction.
        self.__lift_breakdown(self.OK1, self.OK1a, self.SM1x_data)

    @functools.cache
    def __SM2x_setup(self):
        self.SM2x_data = self.__SMx_setup(self.OK2, self.OK2a)
        for I in self.SM2x_data[1]:
            assert self.expo2 == self.ell ** (I.residue_class_degree()) - 1
        self.__lift_breakdown(self.OK2, self.OK2a, self.SM2x_data)

    def __SMx_setup(self, O, Oa):
        """
        Factor ell into pieces, so that we get a chance to compute SMi
        piecewise. Part of the trick is to land on our feet and express
        the result in a basis that remains consistent with SMi.
        While this looks quite cumbersome in sage, this approach is
        actually better complexity-wise.

        O is the maximal order of either K1 or K2, and OKa is the
        maximal order of the corresponding absolute field.

        returns a triple:
            - the breakdown of the defining polynomial of Ka into
              factors, modulo quadratically increasing powers of ell.
              item [i] in the list is factorization modulo ell^(2^i)
            - the factorization of ell in OKa
            - the CRT combiners that are used for the reconstruction

        """
        ell = self.ell

        if O.absolute_discriminant() % ell == 0:
            raise RuntimeError(
                "Out of laziness, we do not compute Schirokauer maps for ramified ell"
            )

        K = O.number_field()
        Ka = Oa.number_field()
        theta = Ka.gen()
        A = Ka.defining_polynomial()

        if A.leading_coefficient() % ell == 0:
            raise RuntimeError(
                "Out of laziness, we do not compute Schirokauer maps when the defining polynomial is not monic"
            )

        Al = A.change_ring(GF(ell))
        Bs = [F for F, m in Al.factor()]

        # breakdown_ell[i] is factorization modulo ell^(2^i)
        breakdown_ell = [Bs]
        breakdown_ideals_ell = []
        # We also pre-compute combiners for the CRT calculation. Note
        # that all this happens only mod ell.
        combiners = []
        for Bl in Bs:
            I = Oa.fractional_ideal(ell, Bl.change_ring(ZZ)(theta))
            assert I.is_prime()
            breakdown_ideals_ell.append(I)
            Cl = Al // Bl
            g, Ul, Vl = Bl.xgcd(Cl)
            combiners.append(Vl * Cl)

        return (breakdown_ell, breakdown_ideals_ell, combiners)

    def __lift_breakdown(self, O, Oa, SMx_data):
        K = O.number_field()
        Ka = Oa.number_field()
        A = Ka.defining_polynomial()
        breakdown_ell, breakdown_ideals_ell, combiners = SMx_data
        ell0 = self.ell ** (2 ** (len(breakdown_ell) - 1))
        ellx = ell0**2
        Bs = breakdown_ell[-1]
        S = Integers(ell0)
        Sx = Integers(ellx)
        Bs0 = [c.change_ring(S) for c in Bs]
        Bsx = [c.change_ring(Sx) for c in Bs]
        prodBsx = prod(Bsx).change_ring(ZZ)
        Rl = ((A - prodBsx) / ell0).change_ring(S)
        Al = A.change_ring(S)
        nn = []
        for i, Bl in enumerate(Bs0):
            SP = Bl.parent()
            SQ = SP.quotient_ring(Bl)
            Cl = prod(Bs0[:i] + Bs0[i + 1 :])
            try:
                g, Ul, Vl = Bl.xgcd(Cl)
            except NotImplementedError:
                g, Ul, Vl = poor_man_xgcd(Bl, Cl)
                assert g.degree() == 0
                s = 1 / g[0]
                Ul *= s
                Vl *= s
                g = 1
            assert g == 1
            # n = SQ(Rl)/SQ(Al/Bl)
            n = SQ(Rl * Vl)
            nn.append(n)
            Bsx[i] += n.lift().change_ring(Sx) * ell0
        breakdown_ell.append(Bsx)
        assert (A - prod(Bsx).change_ring(ZZ)) % ellx == 0

    def SM1x(self, phi):
        """
        This is a special version of SM1 that works even if the norm of
        phi is divisible by ell
        """
        self.__SM1x_setup()  # cached, called only once
        return self.__SMx(self.OK1, self.OK1a, self.SM1x_data, phi) * self.MG1

    def SM2x(self, phi):
        """
        This is a special version of SM1 that works even if the norm of
        phi is divisible by ell
        """
        self.__SM2x_setup()  # cached, called only once
        return self.__SMx(self.OK2, self.OK2a, self.SM2x_data, phi) * self.MG2

    def __SMx(self, O, Oa, SMx_data, phi):
        K = O.number_field()
        Ka = Oa.number_field()
        phi_a = Ka(phi(K.gen()))
        theta = Ka.gen()
        SMx_raw = []
        ell = self.ell

        breakdown_ell, breakdown_ideals_ell, combiners = SMx_data

        for i, I in enumerate(breakdown_ideals_ell):
            v = phi_a.valuation(I)
            while v + 1 >= 2 ** (len(breakdown_ell) - 1):
                # We need to lift more.
                self.__lift_breakdown(O, Oa, SMx_data)
            # which precision do we need for _this reduction exactly_ ?
            # This will be j=1 if v=0, and more generally j will be the
            # smallest integer such that 2^j>(v+1), so j = ceil(log(v+1)/log(2))
            j = (v + 1).bit_length()
            assert j < len(breakdown_ell)
            ellx = self.ell ** (2**j)
            ell1 = self.ell**v
            # Ix is just a polynomial
            Ix = breakdown_ell[j][i]
            # reduce mod ell^(2^j) and mod Ix
            phi_red = phi_a.polynomial().change_ring(Integers(ellx)) % Ix
            phi0 = phi_red.change_ring(ZZ) / ell1
            # Now raise to the correct power. This only happens mod ell^2
            I1 = breakdown_ell[1][i]
            phi1 = phi0.change_ring(Integers(ell**2))
            phi1_y = (phi1 ** (ell ** (I1.degree()) - 1) % I1) - 1
            SMs = phi1_y.change_ring(ZZ) / ell
            SMx_raw.append([SMs[i] for i in range(I1.degree())])

        R = combiners[0].parent()
        SMx_poly = sum([R(c) * combiners[i] for i, c in enumerate(SMx_raw)])

        # The tower representation is a bit cumbersome, but it's the one
        # that SM1 uses internally, so let's stick to it.
        SMx_elem = K(SMx_poly.change_ring(ZZ)(Ka.gen()))
        return vector(GF(ell), sum([list(c) for c in SMx_elem], []))

    def SM1(self, phi):
        alpha = self.K1.gen()
        T = self.KhP.gen()
        phi = phi(alpha)
        phi = sum([phi[i] * T**i for i in range(len(list(phi)))])
        assert phi.parent() is self.KhP
        if self.quicknorm1(phi) % self.ell == 0:
            return self.SM1x(phi)
        phibar = self.R1([self.R(list(c)) for c in list(phi)])
        raised = phibar**self.expo1 - 1
        coeffs = sum([list(c) for c in list(raised)], [])
        # theory mandates that this must be integral
        v = vector(ZZ, vector(QQ, coeffs) / self.ell)
        # base change to our Galois-compatible basis
        # Since we've reduced that matrix mod ell, this includes a reduction
        # modulo ell.
        return v * self.MG1

    def SM2(self, phi):
        alpha = self.K2.gen()
        T = self.KhP.gen()
        phi = phi(alpha)
        phi = sum([phi[i] * T**i for i in range(len(list(phi)))])
        assert phi.parent() is self.KhP
        if self.quicknorm2(phi) % self.ell == 0:
            return self.SM2x(phi)
        phibar = self.R2([self.R(list(c)) for c in list(phi)])
        raised = phibar**self.expo2 - 1
        coeffs = sum([list(c) for c in list(raised)], [])
        # theory mandates that this must be integral
        v = vector(ZZ, vector(QQ, coeffs) / self.ell)
        # base change to our Galois-compatible basis
        # Since we've reduced that matrix mod ell, this includes a reduction
        # modulo ell.
        return v * self.MG2

    def pick_1(self):
        iota = self.Kh.gen()
        alpha = self.K1.gen()
        return sum(
            [
                randint(-2, 2) * iota**i * alpha**j
                for i in range(self.h.degree())
                for j in range(self.f1.degree())
            ]
        )

    def pick_2(self):
        iota = self.Kh.gen()
        beta = self.K2.gen()
        return sum(
            [
                randint(-2, 2) * iota**i * beta**j
                for i in range(self.h.degree())
                for j in range(self.f2.degree())
            ]
        )

    @functools.cache
    def __sm_setup__(self):
        ell = self.ell
        OK1a = self.K1a.maximal_order()
        OK2a = self.K2a.maximal_order()
        ell1 = OK1a.fractional_ideal(ell).factor()
        ell2 = OK2a.fractional_ideal(ell).factor()
        self.expo1 = lcm([ell ** c.residue_class_degree() - 1 for c, k in ell1])
        self.expo2 = lcm([ell ** c.residue_class_degree() - 1 for c, k in ell2])
        self.R = Integers(ell**2)["U"]
        self.Rh = self.R.quotient(self.h, "Ubar")
        self.R1 = self.Rh["V"].quotient(self.f1, "Vbar1")
        self.R2 = self.Rh["V"].quotient(self.f2, "Vbar2")

        # Now we want Galois-compatible bases.
        # We're only really interested in the change of basis matrices, in fact.

        def galois_orbit(sigma, order, gens):
            return sum([[(sigma**i)(e) for i in range(order)] for e in gens], [])

        def is_basis(K, basis):
            """
            This returns the change of basis matrix to the field's default
            basis to this one, or None if the provided basis is not a basis
            """
            M = matrix([vector(K.base_field(), list(K(c))) for c in basis])
            if not M.is_invertible():
                return None
            else:
                return M

        iota = self.Kh.gen()
        alpha = self.K1.gen()
        beta = self.K2.gen()

        good_basis = False
        while not good_basis:
            # G1 = galois_orbit(
            #     self.sigma_K1, self.n, [iota * alpha, iota * (alpha**2 + alpha + 1)]
            # )
            # self.G1 = G1
            # MG1 = is_basis(self.K1a, G1)
            MG1 = None
            while not MG1:
                G1 = galois_orbit(self.sigma_K1, self.n, [self.pick_1(), self.pick_1()])
                self.G1 = G1
                MG1 = is_basis(self.K1a, G1)

            # G2 = galois_orbit(self.sigma_K2, self.n, [iota * beta])
            # self.G2 = G2
            # MG2 = is_basis(self.K2a, G2)
            MG2 = None
            while not MG2:
                G2 = galois_orbit(self.sigma_K2, self.n, [self.pick_2()])
                self.G2 = G2
                MG2 = is_basis(self.K2a, G2)

            # The annoying thing is that our SM maps are expressing things with
            # respect to a basis that is built from the relative field, and it is
            # not a polynomial basis. What we want to get is the chang of basis
            # matrix from this relative basis to our newly created custom basis.
            rel_basis1 = sum(
                [
                    [iota**i * alpha**j for i in range(self.Kh.degree())]
                    for j in range(self.K1.relative_degree())
                ],
                [],
            )
            X1 = is_basis(self.K1a, rel_basis1)
            assert X1
            self.MG1 = X1 * MG1**-1
            rel_basis2 = sum(
                [
                    [iota**i * beta**j for i in range(self.Kh.degree())]
                    for j in range(self.K2.relative_degree())
                ],
                [],
            )
            X2 = is_basis(self.K2a, rel_basis2)
            assert X2
            self.MG2 = X2 * MG2**-1

            # if the MGi cannot be mapped to GF(ell), we start over
            if (
                gcd(self.MG1.denominator(), self.ell) == 1
                and gcd(self.MG2.denominator(), self.ell) == 1
            ):
                good_basis = True

        # we're only interested in what happens mod ell.X²
        self.MG1 = self.MG1.change_ring(GF(self.ell))
        self.MG2 = self.MG2.change_ring(GF(self.ell))
        assert self.MG1.is_invertible()
        assert self.MG2.is_invertible()

        # ah no, this C has rank 1
        # assert self.p**6 % self.ell == 1
        # C = matrix(6, 6, [ GF(self.ell)(self.p)**(i-j) for i,j in itertools.product(range(6), repeat=2) ])
        # self.MG1 *= block_matrix(2,2,[C]*4)
        # self.MG2 *= C

        # This one gives a few globally Galois-invariant maps, but they're
        # unfortunately not Galois-commutative.
        # assert self.p**6 % self.ell == 1
        # C = matrix(6, 6, [ GF(self.ell)(self.p)**(i*j) for i,j in itertools.product(range(6), repeat=2) ])
        # self.MG1 *= block_matrix(2,2,[C]*4)
        # self.MG2 *= C

        self.__SM1x_setup()
        self.__SM2x_setup()

    def __relation_matrices_M(self):
        M1 = matrix(GF(self.ell), len(self.list_phi), len(self.set_ideals_K1))
        M2 = matrix(GF(self.ell), len(self.list_phi), len(self.set_ideals_K2))

        for i, rel in enumerate(self.list_phi):
            phi, fac12 = rel
            fac1, fac2 = fac12
            for j, k in fac1:
                M1[i, j] = k
            for j, k in fac2:
                M2[i, j] = k
        self.M1 = M1
        self.M2 = M2

    def __relation_matrices_S(self):
        S1rows = []
        S2rows = []

        for phi, fac12 in self.list_phi:
            S1rows.append(self.SM1(phi))
            S2rows.append(self.SM2(phi))

        self.S1 = matrix(S1rows)
        self.S2 = matrix(S2rows)

    def __relation_matrices_join(self):
        self.MS1 = block_matrix(1, 2, [self.M1, self.S1])
        self.MS2 = block_matrix(1, 2, [self.M2, self.S2])
        self.MS = block_matrix(1, 2, [self.MS1, self.MS2])

    def relation_matrices(self):
        self.__relation_matrices_M()
        self.__relation_matrices_S()
        self.__relation_matrices_join()
        print(
            f"Full matrix: {self.MS.nrows()} rows {self.MS.ncols()} cols rank {self.MS.rank()}"
        )

    def linear_algebra(self):
        ker = self.MS.right_kernel()
        print(f"Full kernel: {ker}")
        # flag = False
        # for b in ker.basis():
        #     i = 0
        #     while i + 2 < len(b) and b[i] == 0 or b[i + 1] == 0 or b[i + 2] == 0:
        #         i += 1
        #     if b[i + 1] * (b[i]).inverse() == b[i + 2] * (b[i + 1]).inverse():
        #         self.all_vlogs = b
        #         flag = True
        #         break
        # if not flag:
        self.all_vlogs = ker.random_element()
        ll = self.all_vlogs

        print(f"Full kernel vector: {ll.hamming_weight()}/{len(ll)} non-zero logs")
        cut = self.MS.get_subdivisions()[1][0]
        self.all_vlogs1 = self.all_vlogs[:cut]
        self.all_vlogs2 = self.all_vlogs[cut:]
        #print("all vlogs1 :")
        #print(self.all_vlogs1)
        # print("##################### Matrix ##################")
        # print(self.MS)
        # print("***************************")
        # s = "["
        # for i in range(self.MS.nrows()):
        #     s += "["
        #     for j in range(self.MS.ncols()):
        #         s += str(self.MS[i, j]) + ", "
        #     s += "],"
        # s += "]"
        # print(s)
        # print("##########################################################")
        print("info about sub matrices")
        print(
            f"MS1: {self.MS1.nrows()} rows {self.MS1.ncols()} cols rank {(self.MS1).rank()}"
        )
        print(
            f"MS2: {self.MS2.nrows()} rows {self.MS2.ncols()} cols rank {(self.MS2).rank()}"
        )
        assert self.MS * self.all_vlogs == 0
        assert self.MS1 * self.all_vlogs1 + self.MS2 * self.all_vlogs2 == 0

    def to_vector1(self, phi):
        v0 = vector(GF(self.ell), [0] * len(self.set_ideals_K1))
        for c, k in self.OK1.fractional_ideal(phi(self.K1.gen())).factor():
            if c in self.stable_ideals_K1:
                continue
            try:
                v0[self.set_ideals_K1.index(c)] = k
            except KeyError:
                raise NotSmooth(phi, "K1")

        v1 = self.SM1(phi)
        return vector(list(v0) + list(v1))

    def to_vector2(self, phi):
        v0 = vector(GF(self.ell), [0] * len(self.set_ideals_K2))
        for c, k in self.OK2.fractional_ideal(phi(self.K2.gen())).factor():
            if c in self.stable_ideals_K2:
                continue
            try:
                v0[self.set_ideals_K2.index(c)] = k
            except KeyError:
                raise NotSmooth(phi, "K2")

        v1 = self.SM2(phi)
        return vector(list(v0) + list(v1))

    def to_vector1_orbits(self, phi):
        v = self.to_vector1(phi)
        v0 = v[: len(self.set_ideals_K1)]
        v1 = v[len(self.set_ideals_K1) :]
        return vector(
            list(v0 * self.compressor1) + list(v1 * block_diagonal_matrix([self.C] * 2))
        )

    def to_vector2_orbits(self, phi):
        v = self.to_vector2(phi)
        v0 = v[: len(self.set_ideals_K2)]
        v1 = v[len(self.set_ideals_K2) :]
        return vector(list(v0 * self.compressor2) + list(v1 * self.C))

    def vlog_map1(self, phi):
        return self.to_vector1(phi) * self.all_vlogs1

    def vlog_map2(self, phi):
        # We arbitrarily put a minus sign so that in apparence, both vlog
        # maps appear to be equal instead of opposite to eachother
        return -self.to_vector2(phi) * self.all_vlogs2

    def vlog_map1_orbits(self, phi):
        return self.to_vector1_orbits(phi) * self.all_vlogs1_compressed

    def vlog_map2_orbits(self, phi):
        return self.to_vector2_orbits(phi) * self.all_vlogs2_compressed

    def dlog_map(self, phi):
        """
        This is a debug function only.

        Here we reduce to the finite field, and use the finite field DL
        function
        """
        return GF(self.ell)((self.KhP_to_Fpn(phi) ** self.cofac).log(self.logbase))

    def find_smooth_phi_side1(self, exploration_bound):
        assert "smoothness_bound" in self.__dict__
        while True:
            try:
                phi = self.get_phi(exploration_bound)
                return phi, self.vlog_map1(phi)
            except NotSmooth:
                pass

    def find_smooth_phi_side2(self, exploration_bound):
        assert "smoothness_bound" in self.__dict__
        while True:
            try:
                phi = self.get_phi(exploration_bound)
                return phi, self.vlog_map2(phi)
            except NotSmooth:
                pass

    def log_consistency_check(self, ntrials=40):
        ll = self.all_vlogs
        print(f"Log vector: {ll.hamming_weight()}/{len(ll)} non-zero logs")
        quality = ll.hamming_weight() / len(ll)
        if quality < 1 / 2:
            raise RuntimeError(
                "We most probably obtained a trivial log map, something is wrong"
            )

        self.character_ratio = None
        for i in range(ntrials):
            phi, fac = self.list_phi[randrange(len(self.list_phi))]
            d = self.dlog_map(phi)
            if d == 0:
                continue
            v1 = self.vlog_map1(phi)
            v2 = self.vlog_map2(phi)
            assert v1 == v2
            ratio = v1 / d
            if self.character_ratio is None:
                self.character_ratio = ratio
            else:
                print("character ratio = ", self.character_ratio)
                print("ratio = ", ratio)
                assert ratio == self.character_ratio

    def matrix_stats(self):
        print(f"Hamming weight of M1: {len(self.M1.coefficients())}")
        print(f"Hamming weight of M2: {len(self.M2.coefficients())}")
        d = defaultdict(int)
        for v in self.M1.rows():
            d[v.hamming_weight()] += 1
        print(
            "Row weight distribution for M1: "
            + ", ".join([f"{k}: {d[k]}" for k in sorted(d.keys())])
        )
        d = defaultdict(int)
        for v in self.M2.rows():
            d[v.hamming_weight()] += 1
        print(
            "Row weight distribution for M2: "
            + ", ".join([f"{k}: {d[k]}" for k in sorted(d.keys())])
        )
        d = defaultdict(int)
        for v in self.M1.columns():
            d[v.hamming_weight()] += 1
        print(
            "Column weight distribution for M1: "
            + ", ".join([f"{k}: {d[k]}" for k in sorted(d.keys())])
        )
        d = defaultdict(int)
        for v in self.M2.columns():
            d[v.hamming_weight()] += 1
        print(
            "Column weight distribution for M2: "
            + ", ".join([f"{k}: {d[k]}" for k in sorted(d.keys())])
        )

    # This linear algebra call solves a much smaller linear system.
    def modified_linear_algebra(self, d=1):
        print("starting modified_linear_algebra")
        o1 = get_orbits(self.sigma_K1, self.n, self.set_ideals_K1)
        o2 = get_orbits(self.sigma_K2, self.n, self.set_ideals_K2)

        for i, o in enumerate(o1):
            a, b = o
            if matrix(self.M1.columns()[a:b]) != 0:
                continue
            I = self.set_ideals_K1[i]
            p = I.absolute_norm()
            print(f"Info: OK1-ideal of norm {p} was never encountered: {I}")

        for i, o in enumerate(o2):
            a, b = o
            if matrix(self.M2.columns()[a:b]) != 0:
                continue
            I = self.set_ideals_K2[i]
            p = I.absolute_norm()
            print(f"Info: OK2-ideal of norm {p} was never encountered: {I}")

        # setting the right correspondance between the automorphism and the automorphism in the finite field
        iota = self.Kh.gen()
        alpha = self.K1.gen()
        phi_1 = self.pick_1()
        # make sure that phi_1 does not project_to_subfield
        def project_to_subfield(phi):
            proj = self.K1_to_Fpn(phi)
            for div in divisors(self.n)[1:-1]:
                if generic_power(proj, self.p**div) == proj:
                    return True
            return False
        while project_to_subfield(phi_1):
            phi_1 = self.pick_1()

        for i in [k for k in range(1, self.n) if gcd(k, self.n) == 1]:
            if self.K1_to_Fpn(self.sigma_K1(phi_1)) == generic_power(self.K1_to_Fpn(phi_1), self.p**i):
                self.power = i
                print(
                    "######################### Right power #################################"
                )
                print(self.power)
                break
        
        assert self.power
        zeta = GF(self.ell)(self.p)
        self.compressor1 = compressor_from_orbits(zeta, o1, self.power)
        self.compressor2 = compressor_from_orbits(zeta, o2, self.power)

        # This generalizes Schiro
        assert self.n % d == 0
        self.C = matrix(GF(self.ell), self.n, d)
        for j in range(d):
            for i in range(self.n):
                if i % d == j:
                    self.C[i, j] = zeta ** (self.power * i)

        CMS = block_matrix(
            4,
            4,
            [
                self.compressor1,
                0,
                0,
                0,
                0,
                block_diagonal_matrix([self.C] * 2),
                0,
                0,
                0,
                0,
                self.compressor2,
                0,
                0,
                0,
                0,
                self.C,
            ],
        )

        # store the big compressor matrix, it's useful.
        self.CMS = CMS

        # print("##################### Compressed Matrix ##################")
        # print(self.MS * self.CMS)
        # M_prod = self.MS * self.CMS
        # s = "["
        # for i in range(self.MS.nrows()):
        #     s += "["
        #     for j in range(self.CMS.ncols()):
        #         s += str(M_prod[i, j]) + ", "
        #     s += "],"
        # s += "]"
        # print(s)
        # print("##########################################################")
        # print("##################### Compression Matrix ##################")
        # print(self.CMS)
        # print("***********************")
        # s = "["
        # for i in range(self.CMS.nrows()):
        #     s += "["
        #     for j in range(self.CMS.ncols()):
        #         s += str(self.CMS[i, j]) + ", "
        #     s += "],"
        # s += "]"
        # print(s)
        print(
            f"Compressed matrix: {self.MS.nrows()} rows {self.CMS.ncols()} cols rank {(self.MS * self.CMS).rank()}"
        )

        zr = [i for i, r in enumerate((self.MS * CMS).rows()) if r == 0]
        print(f"Compression yields {len(zr)} zero rows: {zr}")

        Cker = (self.MS * CMS).right_kernel()
        print(f"Compressed kernel: {Cker}")

        # print("info about sub matrices")
        # print(
        #     f"MS1: {self.MS1.nrows()} rows {self.MS1.ncols()} cols rank {(self.MS1).rank()}"
        # )
        # print(
        #     f"MS2: {self.MS2.nrows()} rows {self.MS2.ncols()} cols rank {(self.MS2).rank()}"
        # )

        self.all_vlogs_compressed = Cker.random_element()
        self.all_vlogs = CMS * self.all_vlogs_compressed
        cut = self.MS.get_subdivisions()[1][0]
        self.all_vlogs1 = self.all_vlogs[:cut]
        self.all_vlogs2 = self.all_vlogs[cut:]

        # cut_orbits = self.CMS.get_subdivisions()[1][1]
        # self.all_vlogs1_compressed = self.all_vlogs_compressed[:cut_orbits]
        # self.all_vlogs2_compressed = self.all_vlogs_compressed[cut_orbits:]

        ll = self.all_vlogs_compressed
        print(
            f"Compressed kernel vector: {ll.hamming_weight()}/{len(ll)} non-zero logs"
        )
        assert self.MS * self.all_vlogs == 0
        assert self.MS1 * self.all_vlogs1 + self.MS2 * self.all_vlogs2 == 0

        # print(
        #     "#################### vlogs1_compressed ##################################### "
        # )
        # print(self.all_vlogs1_compressed)
        # print(
        #     "#################### vlogs2_compressed ##################################### "
        # )
        # print(self.all_vlogs2_compressed)
        # print("################################################################")

    def unit_maps_stats(self, force=False, d=1):
        if not force:
            d1 = self.K1.absolute_discriminant()
            d2 = self.K2.absolute_discriminant()
            if d1 >= 2**60 or d2 >= 2**60:
                print("Skipping unit computations since discriminants are large")
                return
        print("Computing unit groups")
        U1 = self.K1.units(proof=False)  # units calcule directement des générateurs
        U2 = self.K2.units(proof=False)
        print("Minimum polynomial (in number fields) of units")
        print([self.K1a(self.K1(u)).minpoly() for u in U1])
        print([self.K2a(self.K2(u)).minpoly() for u in U2])
        print("Minimum polynomial (in GF(p^n)) of images of units")
        print([self.K1_to_Fpn(u).minpoly() for u in U1])
        print([self.K2_to_Fpn(u).minpoly() for u in U2])

        if "all_vlogs" in self.__dict__:
            print("Vlog of units_orbits")
            print([self.vlog_map1(self.KhP(list(self.K1(u)))) for u in U1])
            print([self.vlog_map2(self.KhP(list(self.K2(u)))) for u in U2])

            # Adding this to see if our SMs do cancel on units that have
            # non zero vlog
            # Here our SM
            if d==1 or d==2:
                print("Schirokauer maps on units")
                assert self.n % d == 0
                zeta = GF(self.ell)(self.p)
                self.C = matrix(GF(self.ell), self.n, d)
                for j in range(d):
                    for i in range(self.n):
                        if i % d == j:
                            self.C[i, j] = zeta**i
                self.C_double = block_diagonal_matrix([self.C] * 2)
                print([self.SM1(self.KhP(list(self.K1(u)))) * self.C_double for u in U1])
                print([self.SM2(self.KhP(list(self.K2(u)))) * self.C for u in U2])

            # Here usual SM, not necessarily zero of the fixed elements
            else:
                print("Schirokauer maps on units")
                print([self.SM1(self.KhP(list(self.K1(u)))) for u in U1])
                print([self.SM2(self.KhP(list(self.K2(u)))) for u in U2])
            


    def print_primary_info(self):
        print(" p : ", self.p)
        print("ell : ", self.ell)
        print("Polynomial h : ", self.h)
        print("Polynomial f1 : ", self.f1)
        print("Polynomial f2 : ", self.f2)


# vim: ft=python:
