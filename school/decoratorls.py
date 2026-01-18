# def bread(func):
#     def wrapper(): #  *args, **kwargs):
#         print(" <\_______/>")
#         func() #  *args, **kwargs)
#         print(" <\_______/>")
#         return func

#     return wrapper


# @bread
# def ingredients():
#     print(" --помидор--", 
#           " **котлета**",
#           " ----сыр----", 
#           sep = "\n")


# print(ingredients())

    
# import time


# def timer(func):
#     def wrapper(*args, **kwargs):
#         start_timer = time.time()
#         func(*args, **kwargs)
#         end_timer = time.time()
#         result = end_timer - start_timer
#         print(f'{result:.6f}')
#         return func

#     return wrapper


# @timer
# def printing():
#     time.sleep(1)
#     print("Hello, world!")


# printing()


import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args)
        end = time.time()
        print(f'{end-start:.6f}')
        return func

    return wrapper


def repiter(func):
    def wrapper(*args):
        result= []
        for i in range(1000):
            start = time.time()
            func()
            end = time.time()
            result.append(end - start)
        abs_time =  sum(result) / len(result)
        print(abs_time)
        return func
    
    return wrapper


def decorator(func):
    def wrapper(*args, **kwargs):
        print('Печатаю название функции ...')
        func(*args, **kwargs)
        print(f'...название функции {func.__name__} ')
        return func

    return wrapper

@decorator
def print_func():
    print('Hello, world!')


print_func()