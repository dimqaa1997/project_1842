
stop_word = 'stop'
user_answer = ''

print('Эта программа конвертирует продолжительность (единица измерения - секунда) в приемлимый\n'
                        'для человеческого глаза формат времени.\n'
                        'Для выхода их программы напишите мне "stop"\n')

while True:
    user_answer = input('Введите продолжительность: ')
    if user_answer == stop_word.lower():
        break
    else:

        duration = int(user_answer)

        minutes = duration // 60   # Получил общее кол-во минут из секунд
        duration -= minutes * 60

        hour = minutes // 60  # Плоучил часы из минут
        minutes -= hour * 60

        day = hour // 24  # Дни из часов соответственно
        hour -= day * 24

        seconds = duration

        if day > 0:
            print(f'{day} дней, {hour} часов, {minutes} минут, {seconds} секунд')
        elif day == 0 and hour > 0:
            print(f'{hour} часов, {minutes} минут, {seconds} секунд')
        elif hour == 0 and minutes > 0:
            print(f'{minutes} минут, {seconds} секунд')
        else:
            print(f'{seconds} секунд')
print('The End')
