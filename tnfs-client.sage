import tnfs
import io, os, sys
sys.stdout = io.TextIOWrapper(open(sys.stdout.fileno(), 'wb', 0), write_through=True)
sys.stderr = io.TextIOWrapper(open(sys.stderr.fileno(), 'wb', 0), write_through=True)

if __name__ == '__main__':
    TT,data = tnfs.tnfs._unserialize(*sys.argv[1:])
    task = next(data)
    print(f"Task to be done: {task}")
    if task == 'sieve-one-special-q':
        sqside = int(next(data))
        q = ZZ(next(data))
        rh = ZZ(next(data))
        rf = ZZ(next(data))
        radius = float(next(data))
        smoothness_bound = ZZ(next(data))
        R = tnfs.relation_search(TT)
        R.sieve_one_q(sqside, q, rh, rf, radius, smoothness_bound, machine_output=True)
        # for x in R.serialize_result():
        #     print(x)
    else:
        raise RuntimeError(f"Task '{task}' not defined")

