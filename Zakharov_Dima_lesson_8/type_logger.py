# Задание 3
from functools import wraps


def type_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        logger function

        :param args:
        :param kwargs:
        :return:
        """
        func(*args, **kwargs)
        for argument in args:
            print(f"{func.__name__} ({argument}: {type(argument)})", end=", ")
    return wrapper


@type_log
def my_function(num_int, num_float, string, boolean, *args, **kwargs):
    """
    Returns accepted arguments

    :param num_int:
    :param num_float:
    :param string:
    :param boolean:
    :param args:
    :param kwargs:
    :return:
    """
    return num_int, num_float, string, boolean, args, kwargs


if __name__ == '__main__':
    my_function(1, 3.14, 'hi', False, ('Ubuntu', 20.04), ['Windows', 10, 'Home'], {"programming": "language"},
                food='burger', drink='pepsi', python_version=3.8, student_status=True)

    print(f"\n\nName function - {my_function.__name__}\n{my_function.__doc__}")
