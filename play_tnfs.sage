# from sage.misc.cython import cython_import, cython_import_all
# cython_import_all("tnfs.pyx", globals())
import tnfs
import io, os, sys

#examples_6 = [("example6b", dict(p=37, ell=43, E=3, S=1800, q0=200, q1=1800)), ("example6e", dict(p=29, ell=271, E=40, El=14, S=150000, q0=50000, q1=150000)), ("example6e", dict(p=53, ell=919, E=40, El=14, S=400000, q0=100000, q1=400000))]
examples_6 = [
        ("example6b",
         dict(p=37, ell=43, E=3, S=3600, q0=200, q1=1800,
              external_source=[
                  'example6b_37_3_3600.qrels',
                  'example6b_37_3_3600.cube_rels',
                  ])),
        # example6e has quite bulkier polynomials, which explains why it
        # takes more work.
        ("example6e", dict(p=29, ell=271, E=40, El=14, S=150000,
                           q0=50000, q1=150000)),
        ("example6e", dict(p=53, ell=919, E=40, El=14, S=400000,
                           q0=100000, q1=400000))]
examples_12 = [
        ("example12c",
         dict(p=17, E=7, El=4, S=110000,
              q0=50000, q1=150000,
              external_source=['example_12_p_17_auto_18_08_works.qrels',
                               'example_12_p_17_auto_18_08_works.cube_rels'])),
        ("example12",
         dict(p=53, E=6, El=4, S=1048576, q0=500000, q1=1500000))]

attempt = examples_6[0]
use_auto = True # set to False to not use automorphisms
d=1
nb_cores = 1
Date = "11_04_2026"

# attempt = examples_12[0]
# use_auto = True
# d=2
# nb_cores = 1
# Date = "11_09_2024"

if use_auto:
    family, D = attempt
    print("Date : ", Date)
    print("d = ", d)
    D["multithreaded"] = nb_cores
    TT = tnfs.tnfs(family, **D)
    TT.print_primary_info()
    print("Parameters:")
    print(family)
    print(D)
    TT.unit_maps_stats()
    TT.relation_collection(**D)
    # TT.expand_list_phi()  # No automorphisms
    TT.relation_matrices()
    TT.modified_linear_algebra(d=d)  # With automorphisms
    # TT.linear_algebra()  # No automorphisms
    TT.log_consistency_check()
    TT.unit_maps_stats(d=d)
    TT.individual_log_random_elements(ntrials=10)

else:
    family, D = attempt
    print("Date : ", Date)
    print("No use of automorphisms")
    D["multithreaded"] = nb_cores
    TT = tnfs.tnfs(family, **D)
    TT.print_primary_info()
    print("Parameters:")
    print(family)
    print(D)
    TT.unit_maps_stats()
    TT.relation_collection(**D)
    TT.expand_list_phi()  # No automorphisms
    TT.relation_matrices()
    #TT.modified_linear_algebra(d=d)  # With automorphisms
    TT.linear_algebra()  # No automorphisms
    TT.log_consistency_check()
    TT.unit_maps_stats(d=0)  # d=0 just to tell the function that we use the usual Schiro
    TT.individual_log_random_elements(ntrials=10)
