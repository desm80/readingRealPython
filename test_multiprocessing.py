# # Импорт модуля для работы с процессами.
# import multiprocessing
# from time import sleep
#
#
# # Эта функция будет работать в первом процессе.
# def task_1():
#     print('Процесс 1 начал работу')
#     a = 2
#     b = 3
#     result = a + b
#     print(result)
#     for i in range(1, 4):
#         print(f'Инструкция {i} из процесса 1')
#         sleep(1)
#
#     print('Процесс 1 завершил работу')
#
#
# # Эта функция будет работать во втором процессе.
# def task_2():
#     print('Процесс 2 начал работу')
#     text = 'Строчка, которая гуляет сама по себе'
#     print(text)
#     for i in range(1, 4):
#         print(f'Инструкция {i} из процесса 2')
#         sleep(1)
#
#     print('Процесс 2 завершил работу')
#
#
# # Основной поток.
# if __name__ == '__main__':
#     print('Начало работы основного потока')
#
#     # Тут создаются процессы.
#     t1 = multiprocessing.Process(target=task_1)
#     t2 = multiprocessing.Process(target=task_2)
#
#     # Тут процессы запускаются.
#     t1.start()
#     t2.start()
#
#     # Пока все процессы не закончат работу, не продолжат выполняться
#     # инструкции из основного потока.
#     t1.join()
#     t2.join()
#
#     print('Окончание работы основного потока')
# import multiprocessing
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
# if __name__ == '__main__':
#     print('Начало работы основного потока')
#
#     start_time = datetime.now()
#     t1 = multiprocessing.Process(target=task, args=(8,))
#     t2 = multiprocessing.Process(target=task, args=(8,))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     end_time = datetime.now()
#
#     print('Окончание работы основного потока')
#     print(f'Итоговое время выполнения: {end_time - start_time} секунд.')
# import multiprocessing
# from datetime import datetime
#
# import requests
#
#
# def task(number):
#     result = 0
#     value = number ** number
#
#     for i in range(1, value + 1):
#         result += i
#         if i % 1000000 == 0:
#             requests.get('https://python.org')
#
#     print('Среднее арифметическое равно:', result / value)
#
#
# if __name__ == '__main__':
#     print('Начало работы основного потока')
#
#     start_time = datetime.now()
#     t1 = multiprocessing.Process(target=task, args=(8,))
#     t2 = multiprocessing.Process(target=task, args=(8,))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     end_time = datetime.now()
#
#     print('Окончание работы основного потока')
#     print(f'Итоговое время выполнения: {end_time - start_time} секунд.')
import multiprocessing
from random import shuffle

def bogosort(data, process):
    attempt = 1
    while not sorted(data) == data:
        attempt += 1
        shuffle(data)
    print(f'{process} закончил сортировку. Результат: {data}. Количество '
          f'итераций {attempt}.')


if __name__ == '__main__':

    a = [8, 6, 1, 9, 3]
    b = [8, 6, 1, 9, 3]

    process1 = multiprocessing.Process(target=bogosort, args=(a, 'process1'))
    process2 = multiprocessing.Process(target=bogosort, args=(b, 'process2'))
    process2.start()
    process1.start()