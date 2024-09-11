
SetColumns(0);

ZP<x>:=PolynomialRing(Integers());

QR:=FieldOfFractions(ZP);

h:=x^3-x^2-2*x+1;

assert Degree(Gcd(h,Numerator(Evaluate(QR!h,1/(1-QR.1))))) eq Degree(h);
assert Degree(Gcd(h,Numerator(Evaluate(QR!h,1-1/QR.1)))) eq Degree(h);


f1:=x^4+1;

// f1 == (x^2-sqrt(2)*x+1)*(x^2+sqrt(2)*x+1)
// so if p is 1 or 7 mod 8, sqrt(2) is defined mod p, and we can do rational reconstruction to find a palindromic f2


function prime_is_ok_tnfs(p)
    return LegendreSymbol(2,p) eq 1
    and [Degree(x[1]):x in Factorization(h,GF(p))] eq [3]
    and [Degree(x[1]):x in Factorization(f1,GF(p))] eq [2,2];
end function;

p:=79;
assert prime_is_ok_tnfs(p);
ell:=L[#L][1] where L is Factorization(Evaluate(CyclotomicPolynomial(6),p));
assert Gcd(ell, p-1) eq 1;
assert ell mod 6 eq 1;



for i in [1..20] do
    t,uv := RationalReconstruction(i*Sqrt(GF(p)!2));
    if not t then continue; end if;
    uv /:= i;
    break;
end for;
assert t;
u:=Numerator(uv);
v:=Denominator(uv);
assert GF(p)!(u/v)^2 eq 2;

f2:=v*x^2-u*x+v;
f2hat:=x^2-u*x+v^2;

assert Resultant(f1,f2) mod p^2 eq 0;

Kh<iota>:=NumberField(h);
KhP<T>:=PolynomialRing(Kh);
OKh:=MaximalOrder(Kh);
K1<alpha>:=NumberField(ChangeRing(f1,Kh));
K2<vbeta>:=NumberField(ChangeRing(f2hat,Kh));
beta:=vbeta/v;
assert Evaluate(f2, beta) eq 0;


Gh,_,mGh:=AutomorphismGroup(Kh);

sigma_h_gal:=Gh.1;
sigma_h:=mGh(sigma_h_gal);
if sigma_h(iota) ne 1/(1-iota) then
    sigma_h_gal:=Gh.1^2;
    sigma_h:=mGh(sigma_h_gal);
    assert sigma_h(iota) eq 1/(1-iota);
end if;


// sigma6_K1:=hom<K1->K1|e:->Evaluate(f,1/alpha) where f is Polynomial([sigma_h(c) : c in Eltseq(e)])>;
// sigma6_K2:=hom<K2->K2|e:->Evaluate(f,1/alpha) where f is Polynomial([sigma_h(c) : c in Eltseq(e)])>;


K1a:=AbsoluteField(K1);
K2a:=AbsoluteField(K2);

OK1:=MaximalOrder(K1);
OK2:=MaximalOrder(K2);
OK1a:=MaximalOrder(K1a);
OK2a:=MaximalOrder(K2a);


A1a,_,mA1a:=AutomorphismGroup(K1a);
A2a,_,mA2a:=AutomorphismGroup(K2a);

// identification1:=[<a,<K1!mA1a(a)(K1a!x) : x in [iota,alpha]>>:a in A1a];
// identification2:=[<a,<K2!mA2a(a)(K2a!x) : x in [iota,beta] >>:a in A2a];

auto1_images_from_group_element:=func<a|<K1!mA1a(a)(K1a!x) : x in [iota,alpha]>>;
auto2_images_from_group_element:=func<a|<K2!mA2a(a)(K2a!x) : x in [iota,beta]>>;

auto1_group_element_from_images:=AssociativeArray();
for a in A1a do
    auto1_group_element_from_images[auto1_images_from_group_element(a)]:=a;
end for;

auto2_group_element_from_images:=AssociativeArray();
for a in A2a do
    auto2_group_element_from_images[auto2_images_from_group_element(a)]:=a;
end for;

sigma6_K1:=auto1_group_element_from_images[<1/(1-iota),1/alpha>];
sigma6_K2:=auto2_group_element_from_images[<1/(1-iota),1/beta>];

assert Order(sigma6_K1) eq 6;
assert Order(sigma6_K2) eq 6;



Fp3<iota_p>:=ext<GF(p)|h>;
// Fp6<alpha_p>:=ext<GF(p)|f1>;
Fp6<z>:=ext<Fp3|ChangeRing(f2,GF(p))/v>;


K2_to_Fp6:=hom<K2->Fp6|
        e:->Evaluate(Polynomial(Fp6,
            [Fp3|Evaluate(Polynomial(GF(p),Eltseq(c)),iota_p): 
            c in Eltseq(e)]),
            v*z)>;

K1_to_Fp6:=hom<K1->Fp6|
        e:->Evaluate(Polynomial(Fp6,
            [Fp3|Evaluate(Polynomial(GF(p),Eltseq(c)),iota_p): 
            c in Eltseq(e)]),
            z)>;

KhP_to_Fp6:=hom<KhP->Fp6|
        e:->Evaluate(Polynomial(Fp6,
            [Fp3|Evaluate(Polynomial(GF(p),Eltseq(c)),iota_p): 
            c in Eltseq(e)]),
            z)>;

function getphi_generic(B)
    repeat
        phi:=&+[Random(-B,B)*iota^i*T^j : i in [0..2], j in [0..3]];
        phi*:=Sign(LeadingCoefficient(Polynomial(Eltseq(LeadingCoefficient(phi)))));
    until ideal<OKh|Coefficients(phi)> eq ideal<OKh|1>;
    return phi;
end function;

function getphi(B)
    phi:=KhP!0;
    repeat
        a:=ZP![Random(-B,B) : i in [0..2]];
        b:=ZP![Random(-B,B) : i in [0..2]];
        if Gcd(Content(a), Content(b)) ne 1 then continue; end if;
        if b eq 0 then continue; end if;
        b*:=Sign(LeadingCoefficient(b));
        return Evaluate(a,iota)-Evaluate(b,iota)*T;
    // don't remove Kh-duplicates just now
    until false;
    return false;
end function;

function Eltseq_K2(e)
    // given an element of K2, return the coefficients of the polynomial in
    // *beta* that matches this element.
    el:=Coefficients(Evaluate(Polynomial(Eltseq(e)),v*T));
    assert Evaluate(Polynomial(el),beta) eq e;
    return el;
end function;


phi:=getphi(10);


// compute the norms with resultants.
quicknorm1:=func<phi|Integers()!Resultant(Polynomial(Eltseq(Resultant(phi,f1))),h)>;
quicknorm2:=func<phi|Integers()!Resultant(Polynomial(Eltseq(Resultant(phi,f2))),h)>;

assert quicknorm1(phi)/LeadingCoefficient(f1)^Degree(h) eq Norm(K1a!Evaluate(phi,alpha));
assert quicknorm2(phi)/LeadingCoefficient(f2)^Degree(h) eq Norm(K2a!Evaluate(phi,beta));



// first strategy is to pick at random.
/*
smoothness:=400;
for i in [1..100000] do
    phi:=getphi(20); 
    fac1:=Factorization(quicknorm1(phi));
    if Maximum([l[1]:l in fac1]) ge smoothness then continue; end if;
    fac2:=Factorization(quicknorm2(phi));
    if Maximum([l[1]:l in fac2]) ge smoothness then continue; end if;

    // it's nicer of course to print Kh-duplicates with the common stuff
    // removed. Unfortunately it's super messy. And anyway it only makes sense
    // to do as below for principal Kh. Otherwise we can hash on a/b, but it
    // won't catch everything, and leaves open the question of minimality.
    t,gg:=IsPrincipal(&+[ideal<OKh|c>:c in Coefficients(phi)]);
    if t then phi/:=gg; fac1:=Factorization(quicknorm1(phi)); fac2:=Factorization(quicknorm2(phi)); end if;

    print phi, fac1, fac2;

end for;
*/



// second strategy is to enumerate.
B:=5;

// we want to check the orthotope [-B...B]^6.
/* This is a feeble attempt to kill Kh-duplicates proactively, but we reach
 * too few candidates anyway.
function is_in_area(v)
    e:=Eltseq(v);
    return Minimum(e) ge -B and Maximum(e) le B;
end function;
function vec_index(v)
    e:=Eltseq(v);
    return 1+Seqint([c+B:c in e],2*B+1);
end function;

A:=[true : i in [0..(2*B+1)^6-1]];
for pp in PrimesInInterval(1,Minimum(smoothness,Ceiling(B*Sqrt(6)))) do
    // Euclidean norm mustn't exceed B*sqrt(6). Therefore we don't want
    // Bp_bound to exceed B*sqrt(6)/pp.
    Bp_bound:=Floor(B*Sqrt(6)/pp);
    for I in PrimeIdealsOverPrime(Kh, pp) do
        print I, Bp_bound;
        basis:=HKZ(BasisMatrix(I));
        for a0,a1,a2,b0,b1,b2 in [-Bp_bound..Bp_bound] do
            w:=Vector(Eltseq(Vector([a0,a1,a2])*basis) cat Eltseq(Vector([b0,b1,b2])*basis));
            if is_in_area(w) then
                A[vec_index(w)]:=false;
            end if;
        end for;
    end for;
end for;

UKh,mUKh:=UnitGroup(Kh);
smallish_units:=[Kh!mUKh([c:c in x]):x in CartesianProduct([a ne 0 select [0..a-1] else [-10..10] : a in AbelianInvariants(UKh)])];
small_units:=[u:u in smallish_units | Norm(Vector(Eltseq(u))) le B^2];
 */


// ignore:={};
relations:={@@};
smoothness:=1100;

/*
for e in [0..((2*B+1)^6-1) div 2] do
    if not A[e+1] then continue; end if;
    v:=[c-B:c in Intseq(e,2*B+1,6)];
    a0,a1,a2,b0,b1,b2:=Explode(v);
    */
st := 0;
for a0,a1,a2,b0,b1,b2 in [-B..B] do
    if a0 gt 0 then continue; end if;
    a:=Kh![a0,a1,a2];
    b:=Kh![b0,b1,b2];
    if a eq 0 and b ne 1 then continue; end if;
    if a ne 1 and b eq 0 then continue; end if;
    if ideal<OKh|a,b> ne ideal<OKh|1> then
        // printf "Kh-duplicate %o %o\n", a, b;
        continue;
    end if;
    phi:=a-b*T;
    if a-b*T in relations then continue; end if;

    st -:= Cputime();
    fac1:=Factorization(quicknorm1(phi));
    st +:= Cputime();
    if Maximum([0] cat [l[1]:l in fac1]) ge smoothness then continue; end if;
    st -:= Cputime();
    fac2:=Factorization(quicknorm2(phi));
    st +:= Cputime();
    if Maximum([0] cat [l[1]:l in fac2]) ge smoothness then continue; end if;

    if a in Integers() and b in Integers() then
        rel:=a-b*T;
        Include(~relations, rel);
    else
        aa:=sigma_h(a);
        aaa:=sigma_h(aa);
        bb:=sigma_h(b);
        bbb:=sigma_h(bb);

        conj:=[ a-b*T, aa*T-bb, aaa-bbb*T,
                a*T-b, aa-bb*T, aaa*T-bbb
                ];
        /*
        conj:=[ a-b*T];
        */

        for c in conj do
            Include(~relations, c);
            /*
            for u in small_units do
                Include(~ignore, u*c);
            end for;
            */
        end for;
    end if;

    printf "%o %o %o %o\n", Cputime(), st, #relations, phi;
end for;

relations_ideal_ab:=[];

all_ideals_K1:={@@};
all_ideals_K2:={@@};

rows_set:={@@};


for phi in relations do
    fac1:=[];
    fac2:=[];
    for Ik in Factorization(ideal<OK1|Evaluate(phi,alpha)>) do
        I,k:=Explode(Ik);
        Include(~all_ideals_K1, I);
        j:=Index(all_ideals_K1, I);
        Append(~fac1, <j, k>);
    end for;
    for Ik in Factorization(ideal<OK2|Evaluate(phi,beta)>) do
        I,k:=Explode(Ik);
        Include(~all_ideals_K2, I);
        j:=Index(all_ideals_K2, I);
        Append(~fac2, <j, k>);
    end for;
    if <fac1, fac2> in rows_set then continue; end if;
    Include(~rows_set, <fac1, fac2>);
    Append(~relations_ideal_ab, phi);
    printf "%o %o %o\n", phi, fac1, fac2;
end for;

M1:=SparseMatrix(GF(ell), #relations_ideal_ab, #all_ideals_K1);
M2:=SparseMatrix(GF(ell), #relations_ideal_ab, #all_ideals_K2);
for i in [1..#relations_ideal_ab] do
    fac1, fac2:=Explode(rows_set[i]);
    for jk in fac1 do j,k:=Explode(jk); SetEntry(~M1, i, j, k); end for;
    for jk in fac2 do j,k:=Explode(jk); SetEntry(~M2, i, j, k); end for;
end for;


expo1:=Lcm([ell^Degree(x[1])-1:x in Decomposition(OK1a, ell)]);
expo2:=Lcm([ell^Degree(x[1])-1:x in Decomposition(OK2a, ell)]);

RP:=PolynomialRing(Integers(ell^2));
Rh:=quo<RP|h>;
RhP:=PolynomialRing(Rh);

function SM1(phi)
    if Parent(phi) cmpeq K1 then return SM1(KhP!Eltseq(phi)); end if;
    if Parent(phi) cmpeq K1a then return SM1(K1!phi); end if;
    assert Parent(phi) cmpeq KhP;
    R1:=quo<PolynomialRing(Rh)|f1>;
    Rphi:=RhP![Evaluate(RP!Eltseq(c),Rh.1) : c in Eltseq(phi)];

    v1:=Vector([Integers()|Coefficient(Coefficient(blah,j),i): i in [0..Degree(h)-1], j in [0..Degree(K1)-1]] where blah is (Evaluate(Rphi, R1.1)^expo1-1));
    assert IsZero(Vector(GF(ell),v1));
    return Vector(GF(ell), v1 div ell);
end function;

function SM2(phi)
    if Parent(phi) cmpeq K2 then return SM2(KhP!Eltseq(phi)); end if;
    if Parent(phi) cmpeq K2a then return SM2(K2!phi); end if;
    assert Parent(phi) cmpeq KhP;
    R2:=quo<PolynomialRing(Rh)|f2hat>;
    Rphi:=RhP![Evaluate(RP!Eltseq(c),Rh.1) : c in Eltseq(phi)];
    v2:=Vector([Integers()|Coefficient(Coefficient(blah,j),i)*v^j : i in [0..Degree(h)-1], j in [0..Degree(K2)-1]] where blah is (Evaluate(Rphi, R2.1*(1/Integers(ell^2)!v))^expo2-1));
    assert IsZero(Vector(GF(ell),v2));
    return Vector(GF(ell), v2 div ell);
end function;

S1:=Matrix([SM1(phi) : phi in relations_ideal_ab]);
S2:=Matrix([SM2(phi) : phi in relations_ideal_ab]);
MS1:=HorizontalJoin(Matrix(M1),S1);
MS2:=HorizontalJoin(Matrix(M2),S2);


MS:=HorizontalJoin(MS1, MS2);
printf "%o rows %o cols rank %o\n", Nrows(MS), Ncols(MS), Rank(MS);

function centered(x)
    if Category(x) eq SeqEnum then
        return [centered(a):a in x];
    elif Category(x) eq ModTupFldElt then
        return Vector(centered(Eltseq(x)));
    elif Category(x) eq ModTupRngElt then
        return Vector(centered(Eltseq(x)));
    elif Category(x) eq FldFinElt then
        if IsPrimeField(Parent(x)) then
            ell:=#Parent(x);
            xi:=Integers()!x;
            return (xi le ell/2) select xi else -(ell-xi);
        else
            return centered(Eltseq(x));
        end if;
    else
        error Sprintf("argh %o", Category(x));
    end if;
end function;


ker1:=Matrix(Basis(Nullspace(MS1)));
ker2:=Matrix(Basis(Nullspace(MS2)));

/* Here we have a "factory" of ell-th powers. It's not tremendously useful, to
 * be honest.
// this takes a while, but for a baby example it's not much of a problem.
time Lker1:=LLL(Matrix(Integers(),ker1));
time Lker2:=LLL(Matrix(Integers(),ker2));


// we voluntarily take out torsion units, since we know that ell is coprime to
// the torsion order.
//
// Since ell is big, this implies that we're probably not going to get _any_
// non-trivial ell-power out of all this. (especially given the fact that
// we're bounding the euclidean norm of the short vectors we're keeping in the
// result)
ell_th_powers_in_K1:=[];
for i in [1..Nrows(ker1)] do
    r:=Lker1[i];
    if Norm(r) ge 10000 then continue; end if;
    u:=&*[Evaluate(relations_ideal_ab[i],alpha)^r[i]:i in [1..#relations_ideal_ab]|r[i] ne 0];
    if IsTorsionUnit(OK1a!K1a!u) then continue; end if;
    Append(~ell_th_powers_in_K1, u);
end for;

ell_th_powers_in_K2:=[];
for i in [1..Nrows(ker2)] do
    r:=Lker2[i];
    if Norm(r) ge 500 then continue; end if;
    u:=&*[Evaluate(relations_ideal_ab[i],beta)^r[i]:i in [1..#relations_ideal_ab]|r[i] ne 0];
    if IsTorsionUnit(OK2a!K2a!u) then continue; end if;
    Append(~ell_th_powers_in_K2, u);
end for;
*/



ker := NullspaceOfTranspose(MS);
all_vlogs:=Random(ker);
all_vlogs1:=Vector(Eltseq(all_vlogs)[1..Ncols(MS1)]);
all_vlogs2:=Vector(Eltseq(all_vlogs)[Ncols(MS1)+1..Ncols(MS)]);

function dispatch_element_to_vector1(phi)
    if not {@x[1]:x in Factorization(ideal<OK1|Evaluate(phi,alpha)>) @} subset all_ideals_K1 then
        error "the factorization over K1 involves unmet ideals";
    end if;
    v1 := SM1(phi);
    I  := ideal<OK1|Evaluate(phi, alpha)>;
    v0 := [ Valuation(I,pp) : pp in all_ideals_K1 ];
    cofactor_ideal :=I/&*[ all_ideals_K1[i]^v0[i] : i in [1..#all_ideals_K1]];
    assert ideal<OK1a|cofactor_ideal> eq ideal<OK1a|1>;
    return Vector(GF(ell), Eltseq(v0) cat Eltseq(v1));
end function;

function dispatch_element_to_vector2(phi)
    if not {@x[1]:x in Factorization(ideal<OK2|Evaluate(phi,beta)>) @} subset all_ideals_K2 then
        error "the factorization over K2 involves unmet ideals";
    end if;
    v2:=SM2(phi);
    I:=ideal<OK2|Evaluate(phi, beta)>;
    v0 := [ Valuation(I,pp) : pp in all_ideals_K2 ];
    cofactor_ideal :=I/&*[ all_ideals_K2[i]^v0[i] : i in [1..#all_ideals_K2]];
    assert ideal<OK2a|cofactor_ideal> eq ideal<OK2a|1>;
    return Vector(GF(ell), Eltseq(v0) cat Eltseq(v2));
end function;


vlog_map1:=map<KhP->GF(ell)|phi:->(dispatch_element_to_vector1(phi),all_vlogs1)>;
vlog_map2:=map<KhP->GF(ell)|phi:->-(dispatch_element_to_vector2(phi),all_vlogs2)>;
cofac:=(p^6-1) div ell;
// dlog_map:=map<KhP->GF(ell)|phi:->Log(KhP_to_Fp6(phi)^cofac)/cofac>;
dlog_map:=map<KhP->GF(ell)|phi:->Log(KhP_to_Fp6(phi)^cofac)>;

if assigned character_ratio then
    delete character_ratio;
end if;
for i in [1..40] do
    phi:=Random(relations_ideal_ab);
    if dlog_map(phi) eq 0 then
        continue;
        print "got phi with dlog_map == 0, this is weird";
    end if;
    assert vlog_map1(phi) eq vlog_map2(phi);
    ratio := vlog_map1(phi)/dlog_map(phi);
    if assigned character_ratio then
        assert ratio eq character_ratio;
    else
        character_ratio := ratio;
    end if;
end for;

printf "vlog_map{1,2} == %o * dlog_map\n", character_ratio;

function find_smooth_oneside1(B)
    repeat
        phi:=getphi(B); 
        fac1:=Factorization(quicknorm1(phi));
        if not {@x[1]:x in Factorization(ideal<OK1|Evaluate(phi,alpha)>) @} subset all_ideals_K1 then continue; end if;
        vv:=dispatch_element_to_vector1(phi);
        return phi, vv;
    until false;
end function;

procedure matrix_stats()
    print "Hamming weight of M1:", #[x:x in Eltseq(A)|x ne 0] where A is Matrix(M1);
    print "Hamming weight of M2:", #[x:x in Eltseq(A)|x ne 0] where A is Matrix(M2);
    print "Row weight distribution for M1: ", {* #[x:x in Eltseq(A)|x ne 0] : A in Rows(Matrix(M1)) *};
    print "Row weight distribution for M2: ", {* #[x:x in Eltseq(A)|x ne 0] : A in Rows(Matrix(M2)) *};
    print "Column weight distribution for M1: ", {* #[x:x in Eltseq(A)|x ne 0] : A in Rows(Transpose(Matrix(M1))) *};
    print "Column weight distribution for M2: ", {* #[x:x in Eltseq(A)|x ne 0] : A in Rows(Transpose(Matrix(M2))) *};
end procedure;

/*
 * some debug code below...
 *

Write("/tmp/M1.txt", Eltseq(Matrix(M1)));
Write("/tmp/M2.txt", Eltseq(Matrix(M2)));
Write("/tmp/S1.txt", Eltseq(S1));
Write("/tmp/S2.txt", Eltseq(S2));
Write("/tmp/V.txt", Eltseq(all_vlogs));

// try to reverse-engineer what we have on the K1 / K1a side.
U1a,mU1a:=UnitGroup(K1a);
U2a,mU2a:=UnitGroup(K2a);
matSM1units:=Matrix([SM1(K1!mU1a(U1a.i)):i in [1..Ngens(U1a)]]);
matSM2units:=Matrix([SM2(K2!mU2a(U2a.i)):i in [1..Ngens(U2a)]]);

function reorganize_SM_matrix_on_units(M)
    EE,TT := EchelonForm(M);
    Ugens := [];
    for i in [1..Nrows(EE)] do
        r:=EE[i];
        if IsZero(r) then continue; end if;
        j := Minimum([j:j in [1..Ncols(EE)]|r[j] ne 0]);
        Append(~Ugens, < TT[i], j >);
    end for;
    return Ugens;
end function;

magic_set_1:=reorganize_SM_matrix_on_units(matSM1units);


function SM1x(phi)
    w:=Eltseq(SM1(phi));
    return Vector([w[i[2]] : i in magic_set_1]);
end function;

matSM1xunits:=Matrix([SM1x(K1!mU1a(U1a.i)):i in [1..Ngens(U1a)]]);
assert Rank(matSM1xunits) eq Rank(matSM1units);

print "computing generators of ideals";
gens1_raw:=[];
gens1:=[];
for I in all_ideals_K1 do
    Ia:=ideal<OK1a|I>;
    t,g:=IsPrincipal(Ia);
    assert t;
    g:=K1!g;
    Append(~gens1_raw, g);
    vv1 := centered(Solution(matSM1xunits,SM1x(g)));
    g/:=K1!mU1a(U1a!Eltseq(vv1));
    assert ideal<OK1|g> eq I;
    Append(~gens1, g);
end for;

CC:=ComplexField(10^6);
RR:=RealField(CC);
rootsK1:=[r[1]:r in Roots(DefiningPolynomial(K1a), CC)];

// if this overflows, we're not good...
logmap:=hom<K1a->VectorSpace(RR, Degree(K1a))|
    e:->[
        Log(AbsoluteValue(Evaluate(Polynomial(Eltseq(e)), r))) : r in rootsK1]>;

logunitlattice1:=Lattice(Matrix([logmap(mU1a(U1a.i)):i in [1..Ngens(U1a)]]));



function test(phi)
    v1 := SM1(phi);
    I  := ideal<OK1|Evaluate(phi, alpha)>;
    v0 := [ Valuation(I,pp) : pp in all_ideals_K1 ];
    synth := &*[ gens1[i]^v0[i] : i in [1..#all_ideals_K1]  | v0[i] ne 0];
    logmap_of_synth:=&+[ v0[i]*logmap(gens1[i]) : i in [1..#all_ideals_K1] | v0[i] ne 0];
    combination_of_units:=centered(&+[v1[uj[2]]*uj[1] : uj in magic_set_1]);
    logmap_of_combination:=CoordinatesToElement(logunitlattice1,combination_of_units);
    synth2 := K1!mU1a(U1a!Eltseq(combination_of_units));


    // synth*synth2/mU1a(U1a!Coordinates(ClosestVector(logunitlattice1, (logmap_of_synth+Vector(logmap_of_combination))/ell)))^ell; 


    // synth *:= &*[ uj[1]^centered(v1[uj[2]]) : uj in magic_set_1 ];
    vv1:=v1 - SM1(synth);
    //// combination_of_units:=centered(&+[vv1[uj[2]]*uj[1] : uj in magic_set_1]);
    assert &and [vv1[uj[2]] eq v1[uj[2]] : uj in magic_set_1];
    cof:= Evaluate(phi,alpha) / synth / synth2;
    w := SM1(cof);
    return w, cof;
    // print v1;
    // print w;
    // vv1 := [centered(a):a in Eltseq(Solution(matSM1units,w))];
    // print vv1;
    // ncof:=K1!mU1a(U1a!vv1);
    // return Vector(GF(ell), Eltseq(v0) cat Eltseq(v1)), cof/ncof;
end function;


// for phi in relations_ideal_ab do v,cof:=dispatch_element_to_vector1_gen(phi); assert IsTorsionUnit(OKh!Norm(cof)); end for;


w,cof:=test(relations_ideal_ab[10]);
AbsoluteNorm(cof);

// Root(cof, ell);

*/
