# powerful tools for modifying or extending behavior without changing code
# add functionality
import time

def time_taken(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Executing {func.__name__}...")
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken: {end_time - start_time} seconds")
    return wrapper
    
def my_decorator(func):
    def wrapper():
        print("Before function is called")
        func()
        print("After function is called")
    return wrapper

@my_decorator
def say_hello():
    print('Hello!')

# say_hello() # Hello!

@time_taken
def add(a, b):
    print("a is ", a)
    print("b is ", b)
    sum = a + b
    print("Sum is ", sum)

add(10, 12)
