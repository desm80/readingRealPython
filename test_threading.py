# import threading
# # Импорт функции для реализации паузы между инструкциями.
# from time import sleep
#
#
# def task_1():
#     print('Поток 1 начал работу')
#     a = 2
#     b = 3
#     result = a + b
#     print(result)
#     # Вот они — дополнительные инструкции для первого потока.
#     for i in range(1, 4):
#         print(f'Инструкция {i} из потока 1')
#         sleep(1)
#
#     print('Поток 1 завершил работу')
#
#
# def task_2():
#     print('Поток 2 начал работу')
#     text = 'Строчка, которая гуляет сама по себе'
#     print(text)
#     # Дополнительные инструкции для второго потока.
#     for i in range(1, 4):
#         print(f'Инструкция {i} из потока 2')
#         sleep(1)
#
#     print('Поток 2 завершил работу')
#
#
# # Основной поток.
# if __name__ == '__main__':
#     print('Начало работы основного потока')
#
#     t1 = threading.Thread(target=task_1)
#     t2 = threading.Thread(target=task_2)
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#
#     print('Окончание работы основного потока')
# import threading
# from datetime import datetime
#
#
# def task(number):
#     result = 0
#     value = number ** number
#
#     for i in range(1, value + 1):
#         result += i
#     print('Среднее арифметическое равно:', result / value)
#
#
# if __name__ == '__main__':
#     print('Начало работы основного потока')
#
#     start_time = datetime.now()
#     # При создании экземпляра класса Tread указывается два параметра:
#     # target — название функции,
#     # args — аргумент для этой функции, в нашем случае это значение n.
#     # Кортеж из одного элемента должен заканчиваться запятой.
#     t1 = threading.Thread(target=task, args=(8,))
#     t2 = threading.Thread(target=task, args=(8,))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     end_time = datetime.now()
#
#     print('Окончание работы основного потока')
#     print(f'Итоговое время выполнения: {end_time - start_time} секунд.')
import threading
from datetime import datetime

import requests


def task(number):
    result = 0
    value = number ** number

    for i in range(1, value + 1):
        result += i
        if i % 1000000 == 0:
            requests.get('https://python.org')

    print('Среднее арифметическое равно:', result / value)


if __name__ == '__main__':
    print('Начало работы основного потока')

    start_time = datetime.now()
    t1 = threading.Thread(target=task, args=(8,))
    t2 = threading.Thread(target=task, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time = datetime.now()

    print('Окончание работы основного потока')
    print(f'Итоговое время выполнения: {end_time - start_time} секунд.')