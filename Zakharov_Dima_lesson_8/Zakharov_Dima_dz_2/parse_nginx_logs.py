# Задание 2
import re
from time import time


def parse_log(string_log):
    pattern_3 = re.compile(
        r"(\d{2}\.\d+\.\d+\.\d+)|(?<=\[)(\d+\/[A-Za-z]+\/\d{4}[\:\d+]+\s\+\d{4})(?=\])|(?<=\")([A-Z]{3,4})|"
        r"(?<=\s)(\/[a-z]+\/[a-z]+\_\d\s[A-Z]+\/\d\.\d)(?=\")|(?<=\s)(\d+)(?=\s)")
    temp_list = list()
    match = pattern_3.findall(string_log)
    for element in match:
        for el in element:
            if el:
                temp_list.append(el)
    return tuple(temp_list)


if __name__ == '__main__':
    start_point = time()
    result_list = list()
    with open("nginx_logs.txt", "r", encoding="utf-8") as fp:
        for line in fp:
            parsed_element = parse_log(line)
            result_list.append(parsed_element)
    print(result_list)
    print(time() - start_point)
