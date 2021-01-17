import functools
import time


def timer(func):
    @functools.wraps(func)
    def wraps(*args, **kwargs):
        print(f"{func.__name__} Function Start running...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} Function running time: {(end - start) * 1000:.2f} ms")
        return result

    return wraps


@timer
def test(num):
    for i in range(num):
        print("run in {}".format(i))
        time.sleep(1)


test(3)