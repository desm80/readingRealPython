# import threading
# from datetime import datetime
#
# import requests
#
#
# # Функция с GET-запросом.
# def task(task_id):
#     response = requests.get('https://python.org')
#     response_html = response.text
#     # Вывод на печать первых 15 символов ответа от сервера.
#     print(response_html[:15])
#     # Вывод сообщения после выполнения GET-запроса.
#     print(f'Задача {task_id} выполнена.')
#
#
# # Функция, которая десять раз подряд запускает функцию с GET-запросом.
# def sync_execute():
#     tasks = []
#     # Чтобы не создавать десять потоков отдельно,
#     # запускается цикл, и потоки создаются в нём.
#     for i in range(1, 11):
#         # Каждый запрос к сайту должен выполняться в отдельном потоке.
#         tasks.append(threading.Thread(target=task, args=(i,)))
#     # Запуск дочерних потоков в цикле.
#     for t in tasks:
#         t.start()
#
#     # Пока не выполнятся все дочерние потоки,
#     # программа не начнёт выполнять основной поток.
#     for t in tasks:
#         t.join()
#
#
# if __name__ == '__main__':
#     print('Последовательное выполнение кода:')
#     # Фиксируется время начала выполнения программы.
#     start_time = datetime.now()
#     # Выполняется функция sync_execute().
#     sync_execute()
#     # Фиксируется время окончания выполнения программы.
#     end_time = datetime.now()
#     # Выводится итоговое время выполнения программы.
#     print(f'Итоговое время выполнения: {end_time - start_time} секунд.')



# import asyncio
# from datetime import datetime
#
#
# import aiohttp
#
#
# async def task(task_id):
#     async with aiohttp.ClientSession() as session:
#         response = await session.get('https://python.org')
#         response_html = await response.text()
#         print(response_html[:15])
#     print(f'Задача {task_id} выполнена.')
#
#
# async def async_execute():
#     tasks = [asyncio.ensure_future(task(i)) for i in range(1, 11)]
#     await asyncio.wait(tasks)
#
#
# if __name__ == '__main__':
#
#     myloop = asyncio.get_event_loop()
#     print('Асинхронное выполнение кода:')
#     start_time = datetime.now()
#
#     myloop.run_until_complete(async_execute())
#     myloop.close()
#
#     end_time = datetime.now()
#     print(f'Итоговое время выполнения: {end_time - start_time} секунд.')

import asyncio
from datetime import datetime

import aiohttp


async def task(task_id):
    async with aiohttp.ClientSession() as session:
        response = await session.get('http://python.org')
        response_html = await response.text()
        print(response_html[:15])
    print(f'Задача {task_id} выполнена.')


async def async_execute():
    tasks = [asyncio.ensure_future(task(i)) for i in range(1, 11)]
    await asyncio.wait(tasks)


if __name__ == '__main__':
    print('Асинхронное выполнение кода:')
    start_time = datetime.now()

    # Одна строчка кода заменяет три.
    asyncio.run(async_execute())

    end_time = datetime.now()
    print(f'Итоговое время выполнения: {end_time - start_time} секунд.')