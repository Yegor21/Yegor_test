print(type(7))
print(type('hello'))
print(type(str))
print(type(9.99))
print(type({9.99}))
print(type({"num1": "234"}))
print(type(["apple", "banana", "cherry"]))
print(type(True))
print(type(None))

# 1

num = -1.6
int_round = round(num)
print(int_round)

num = 2.99
int_round = round(num)
print(int_round)

# 2
site = 'www.my_site.com#about'
s1 = site.replace('#', '/', )
print(s1)

# 3
word_1 = 'stroka'
word_2 = word_1 + 'ing'
print(word_2)

# 4

str_fio = 'Ivanou Ivan'
k = str_fio.split(' ')
print(k[1] + ' ' + k[0])

# 5

str_fio = ' Yegor Osipik '
str_fio.strip(' ')
print(str_fio.strip(' '))

# 6

dict = {'1A': '30', '1B': '28', '1C': '23', '1D': '25', '2A': '31',
        '2B': '27', '2C': '26', '2D': '29', '3A': '30',
        '3B': '24'}
school = dict
print(school)

# 7
x = [3, 9.5, 'Python', 999999]
print(x[1])

# 8

str_1 = 'employ'
str_2 = 'employment'
if str_2.__contains__(str_1):
    print('Да, \nвходит.')
else:
    print('Нет, \nне входит')

# 9

x = "My name is Agent Smith"
print(x[1])  # y
print(x[3:18:3])  # nesgt

# lst_str = ['один', 'два', 'три', 'четыре']
# lst_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(dict(zip(lst_num, lst_str)))


