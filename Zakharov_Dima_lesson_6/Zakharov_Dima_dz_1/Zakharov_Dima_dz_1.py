import sys


def get_result(string_log):
    log_list = string_log.split()
    for _ in range(4):
        del log_list[1]
    user_ip = log_list[0]
    request_type = log_list[1].strip('"')
    requested_resource = log_list[2]
    res = (user_ip, request_type, requested_resource)
    return res

    # print(log_list)


if __name__ == '__main__':
    result_list = list()
    with open('nginx_logs.txt', 'r', encoding='utf-8') as fp:
        for line in fp:
            res_tuple = get_result(line)
            result_list.append(res_tuple)
            # print(res_tuple, type(res_tuple))
    print(result_list, type(result_list))