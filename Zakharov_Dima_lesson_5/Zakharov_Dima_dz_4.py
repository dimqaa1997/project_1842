src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def get_num(number_list):
    count = 0
    for num in src:
        if num == src[0]:
            count += 1
            continue
        if num > src[count - 1]:
            yield num
        count += 1


if __name__ == '__main__':
    res = get_num(src)
    print(next(res), next(res), list(res), type(res), sep='\n')
