from random import choice


def get_jokes(num):
    """
    Generates jokes
    :param num:
    :return: list of jokes
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    result_list = list()

    for i in range(num):
        element = f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}'
        result_list.append(element)

    return result_list


if __name__ == "__main__":
    user_answer = int(input())
    result = get_jokes(user_answer)
    print(result)
