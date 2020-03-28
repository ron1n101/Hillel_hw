"""
2. Имеется строка вида: AABABBAABBBAB. Необходимо написать функцию которая заменит буквы A на B, а B, соответственно,
на A. Замену можно производить ТОЛЬКО используя функцию replace(). В результате применения функции к исходной строке,
функция должна вернуть строку: BBABAABBAAABA
"""










def change(string):
    print('Исходный текст:  ',string)
    new_string = []
    for i in range(len(string)):
        if string[i] == 'A':
            new_string.append(string[:1].replace('A','B'))
            pass
        elif string[i] == 'B':
            new_string.append(string[:1].replace('B', 'A'))
            pass
    return ''.join(new_string)

print("То что получилось: ", change('AABABBAABBBAB'))




