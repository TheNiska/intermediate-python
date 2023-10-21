from timeit import timeit


def get_time(func, *args, NUM=1000, **kwargs) -> float:
    statement = "func(*args, **kwargs)"
    variables = {'func': func, 'args': args, 'kwargs': kwargs}
    time = timeit(stmt=statement, globals=variables, number=NUM)
    return time
