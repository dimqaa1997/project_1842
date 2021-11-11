# Задание 1
import re


def email_validation(email_address):
    valid_reg_exp = re.compile(r"[\w]+\.{0,}\w{0,}@\w+\.\w+")
    match = valid_reg_exp.fullmatch(email_address)
    if match:
        res = re.split('@', email_address)
        res_dict = dict()
        res_dict['username'] = res[0]
        res_dict['domain'] = res[-1]
        return res_dict
    else:
        raise ValueError(f"wrong email {email_address}")


if __name__ == '__main__':
    print(email_validation(input("Enter your email: ")))
