import time


def time_elapsed(func):

    def time_elapsed_wrapper(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start} seconds")
        return value

    return time_elapsed_wrapper


@time_elapsed
def calc_sum():
    sum=0
    for i in range(10000000):
        sum+=i
    return sum

calc_sum()


def calc_sum2():
    sum = 0
    for i in range(10000000):
        sum += i
    return sum


class my_timer():
    def __init__(self):
        self.start = time.time()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        runtime = self.end - self.start
        msg = 'The function took {time} seconds to complete'
        print(msg.format(time=runtime))


with my_timer():
    calc_sum2()



