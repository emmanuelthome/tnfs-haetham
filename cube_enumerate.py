from copy import copy

def cube_enumerate(n, B):
    def S(i0, i1, w, cc=[1]):
        if w == 0:
            yield []
        else:
            for i in range(i0, i1):
                for s in S(i+1, i1, w-1, cc=cc):
                    for c in cc:
                        yield [(i,c)] + s
    if B == 0:
        yield (0,) * n
    else:
        for w in range(0, n+1):
            for facet in S(0, n, w, [-B,B]):
                s0 = [0]*n
                for f,c in facet:
                    s0[f] = c
                com = set(range(n)) - set([f[0] for f in facet])
                for e in cube_enumerate(n-w, B-1):
                    s = copy(s0)
                    for i,j in enumerate(com):
                        s[j] = e[i]
                    yield tuple(s)

