import contextlib
import time

@contextlib.contextmanager
def time_print(task_name):
    t = time.time()
    try:
        yield
    finally:
        print(task_name, "took", time.time() - t, "seconds.")


def doproc():
    x=1+1


with time_print("processes"):
    [doproc() for _ in range(500000)]

# processes took 15.236166954 seconds.