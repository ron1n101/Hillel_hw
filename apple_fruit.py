"""
3. Дан словарь ключами которого являются английские слова, а значениями - списки латинских слов.
Необходимо развеннуть словарь. Другими словани, необходимо, на основании заданного словаря, создать новый словарь,
у которого в качестве ключей будут взяты латинские слова, из первого словаря, а значениями будут, соответствующие
им, английские слова.
"""

from pprint import pp
d = {
    'apple': ['malum', 'pomum', 'popula'],
    'fruit': ['baca', 'bacca', 'popum'],
    'punishment': ['malum', 'multa']
}
dct_new = {}
dct_new['apple'] = ['malum', 'pomum', 'popula']
dct_new['fruit'] = ['baca', 'bacca', 'popum']
dct_new['punishment'] = ['malum', 'multa']
pp(dct_new)

pp('*' * 100)

d_new = {}

for key,value in dct_new.items():
    for value2 in value:
        d_new[value2] = key
pp(d_new)

