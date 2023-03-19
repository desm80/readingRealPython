# def cube(x: int):
#     """Возвращает число возведенное в степень 3."""
#     return f'Кубом числа {x} является {pow(x, 3)}'
#
#
# def greet(name: str):
#     """Возвращает приветствие по имени"""
#     return f'Hello, {name}!'
#
#
# print(cube(2))
# print(greet('Den'))


# def convert_cel_to_far(c: int):
#     """Temperature converter"""
#     print(f'{c} degrees C = {(int(c) * 9/5) + 32:.2f} degrees F')
#
#
# def convert_far_to_cel(f: int):
#     """Temperature converter"""
#     print(f'{f} degrees F = {(int(f)-32) * 5/9:.2f} degrees C')
#
#
# convert_far_to_cel(input('Enter a temperature in degrees F: '))
# convert_cel_to_far(input('Enter a temperature in degrees C: '))

# def invest(amount, rate, years):
#     """Расчет сложного процента по вкладу"""
#     for year in range(1, years + 1):
#         amount = amount * (rate + 1)
#         print(f'year {year}: ${amount:,.2f}')
#
#
# invest(100000, 0.05, 10)


num = int(input('Введите число: > '))

for i in range(1, num+1):
    if num % i == 0:
        print(f'{i} является делителем числа {num}')


