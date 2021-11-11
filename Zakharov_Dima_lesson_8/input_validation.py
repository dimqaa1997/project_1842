# Задание 4
from functools import wraps


def input_validation(check_valid):
    def inner_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            msg = f'невозможно выполнить {args[0]}'
            if check_valid(*args):
                func(*args)
            else:
                raise ValueError(msg)
        return wrapper
    return inner_dec


@input_validation(lambda x: x > 0)
def buy_apple(number):
    print(f'Give me {number} apples')


if __name__ == '__main__':
    buy_apple(-5)
