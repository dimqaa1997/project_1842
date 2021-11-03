import json


def write_data(price):
    with open('bakery.csv', 'a+', encoding='utf-8') as fp:
        fp.seek(0)
        string_price = sum(1 for _ in fp)
        key = string_price + 1
        new_entry = {key: price}
        fp.write(json.dumps(new_entry) + '\n')


def get_data(start_number=None, end_number=None):
    with open('bakery.csv', 'r', encoding='utf-8') as fp:

        if start_number and end_number:
            key_start = int(start_number)
            ket_end = int(end_number) + 1
            for line in fp:
                entry = json.loads(line)
                if entry.get(str(key_start)) and entry.get(str(key_start)) != entry.get(str(ket_end)):
                    print(entry[str(key_start)])
                    key_start += 1

        elif start_number:
            key = int(start_number)
            for line in fp:
                entry = json.loads(line)
                if entry.get(str(key)):
                    print(entry[str(key)])
                    key += 1

        else:
            for line in fp:
                entry = json.loads(line)
                value = list((value for value in entry.values()))
                print(value[0])


if __name__ == '__main__':
    get_data("5", "7")
