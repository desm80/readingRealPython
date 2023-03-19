# from random import shuffle
#
#
# # Функция, которая перемешивает элементы списка, пока они не будут упорядочены.
# def bogosort(data):
#     # Начинается подсчёт количества попыток.
#     attempt = 1
#     # Цикл, в котором сортируется список.
#     while not sorted(data) == data:
#         # Выводится номер попытки.
#         print('Попытка #', attempt)
#         # Счётчик попыток увеличивается на единицу.
#         attempt += 1
#         # Перемешивается список при помощи функции shuffle.
#         shuffle(data)
#     return data
#
#
# if __name__ == '__main__':
#     # # Набор чисел для перемешивания.
#     # a = [5, 2, 6, 4]
#     # print(bogosort(a))
#     # Новый набор чисел для перемешевания.
#     a = [8, 6, 1, 9, 3, 7, 2, 5, 4]
#     print(bogosort(a))
#     # Новая независимая команда.
#     print('Строчка, которая гуляет сама по себе')
# from datetime import datetime
#
#
# # Функция с расчётом среднего арифметического.
# def task(number):
#     result = 0
#     value = number ** number
#
#     for i in range(1, value + 1):
#         result += i
#     return result / value
#
#
# if __name__ == '__main__':
#     print('Начало работы основного потока')
#     # Фиксируется время начала выполнения программы.
#     start_time = datetime.now()
#     print(task(8))
#     print(task(8))
#     # Фиксируется время окончания выполнения программы.
#     end_time = datetime.now()
#
#     print('Окончание работы основного потока')
#     print(f'Итоговое время выполнения: {end_time - start_time} секунд.')
from datetime import datetime

import requests


def task(number):
    result = 0
    value = number ** number

    for i in range(1, value + 1):
        result += i
        if i % 1000000 == 0:
            # Вот он GET-запрос.
            requests.get('https://python.org')

    print('Среднее арифметическое равно:', result / value)


if __name__ == '__main__':
    print('Начало работы основного потока')

    start_time = datetime.now()

    task(8)
    task(8)

    end_time = datetime.now()

    print('Окончание работы основного потока')
    print(f'Итоговое время выполнения: {end_time - start_time} секунд.')