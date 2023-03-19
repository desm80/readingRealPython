# lines =['   Fnbjb jgjg', 'Fkhkj    ', '  Gjhjhj   ']
# lines = [line.strip() for line in lines]
# print(lines)

# strings = ['Becomes', 'becomes', 'BEAR', 'bEautiful']
# strings = [string.lower().startswith('be') for string in strings]
# print(strings)
#
# while True:
#     letters = input('Tell me your password: ')
#     try:
#         print(
#             f'The first letter you entered was : {letters[0].upper()} {len(letters)}')
#     except Exception:
#         print('вы ничего не ввели')

# a = input('Введите первое число>')
# b = input('Введите второе число>')
# print(float(a)*float(b))

# CODE = {
#     'a': '4',
#     'b': '8',
#     'e': '3',
#     'l': '1',
#     'o': '0',
#     's': '5',
#     't': '7',
# }
#
# text = input('Enter some text:>')
#
# for key, value in CODE.items():
#     text = text.replace(key, value)
# print(text)


from pprint import pprint

data = \
'''Mike Smith,15554218841,123 Nice St, Roy, NM, USA
Anita Hernandez,15557789941,425 Sunny St, New York, NY, USA
Guido van Rossum,315558730,Science Park 123, 1098 XG Amsterdam, NL'''

new_data = []
for string in data.split('\n'):
    new_data.append(string.split(',', maxsplit=2))

pprint(new_data)
