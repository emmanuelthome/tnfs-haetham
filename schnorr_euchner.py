from sage.matrix.constructor import matrix
from sage.rings.real_mpfr import RR
from math import sqrt
from sage.functions.other import ceil, floor
from sage.modules.free_module_element import vector

class SchnorrEuchnerEnumeration(object):
    def __init__(self, M, R):
        """
        Initializes an enumeration process that lists all lattice vectors
        or square-norm less than R^2
        """
        self.M = M
        self.R = R
        self.n = M.nrows()
        self.LM = M.LLL()
        self.G,self.T = self.LM.gram_schmidt()
        GR = self.G.change_ring(RR)
        self.sqnorms_bi_star = (GR*GR.transpose()).diagonal()

        #  bi_star = G
        #  mu_i = T
        #  for i in range(self.n):
        #      assert mu_i[i,i] == 1
        #      assert M[i] == sum([mu_i[i,j]*bi_star[j] for j in range(i+1)])

    def enum(self):
        self.vectors = []
        self._enum_internal([], 0)
        return self.vectors

    def _enum_internal(self, tail, projected_norm):
        k = self.n - len(tail) - 1
        # print(f"Entering enumeration for v[{k}], tail={tail}, proj={projected_norm}")
        # get the bound on the sum |v_k + sum(tail[i] * T[i,k] for i in
        # range(k,n))
        rem = self.R**2 - projected_norm
        if rem < 0:
            return
        local_bound = sqrt(rem/self.sqnorms_bi_star[k])
        shift = sum([t*self.T[i+k+1,k] for i,t in enumerate(tail)])
        # print(f"v[{k}] can be between {-local_bound-shift:.1f} and {local_bound-shift:.1f}")
        lower_bound = ceil(-local_bound-shift)
        upper_bound = floor(local_bound-shift)
        if vector(tail) == 0:
            if upper_bound >= 1:
                lower_bound = 0
        for v in range(lower_bound, upper_bound+1):
            if k:
                nproj = projected_norm + (v + shift)**2*self.sqnorms_bi_star[k]
                self._enum_internal([v]+tail, nproj)
            else:
                self.vectors.append(vector([v] + tail)*self.LM)

if __name__ == '__main__':
    Lq = matrix([(587, 0, 0, 0, 0, 0),
                 (-383, 1, 0, 0, 0, 0),
                 (0, -383, 1, 0, 0, 0),
                 (-461, 0, 0, 1, 0, 0),
                 (0, -461, 0, 0, 1, 0),
                 (0, 0, -461, 0, 0, 1)])
    S = SchnorrEuchnerEnumeration(Lq, 6)
    A = S.enum()
    for v in A:
        print(v)
    print(f"Found {len(A)} vectors")


