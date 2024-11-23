import time

def time_logger(func):
    def wrapper(*args,**kwargs):
        start_time = time.perf_counter()
        result = func(*args,**kwargs)
        end_time = time.perf_counter()
        print(f"Function {func.__name__} took {(end_time - start_time)} seconds to execute")
        return result
    return wrapper
    