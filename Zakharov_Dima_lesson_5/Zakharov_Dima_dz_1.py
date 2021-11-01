import sys


def get_odd_numbers(end):
    for num in range(1, end + 1, 2):
        yield num


if __name__ == '__main__':
    res = get_odd_numbers(15)
    print(type(res), sys.getsizeof(res), next(res), next(res), next(res), list(res), sep='\n')
