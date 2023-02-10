print(type(7))
print(type('hello'))
print(type(str))
print(type(7))
print(type(9.99))

num = -1.6
int_round = round(num)
print(int_round)

num = 2.235566470338304765
f_r = round(num, 5)
print(f_r)

# 3
spisok = [123, 'dfr', 'p812']
print(spisok)

# 4
site = 'www.my_site.com#about'
s1 = site.replace('#', '/', )
print(s1)

# 5
word_1 = 'stroka'
word_2 = word_1.replace('a', 'ing')
print(word_2)

# 6

fio = "Ivanou Ivan"
f_2 = fio.replace("Ivanou", "Ivan")
# f_3 = fio.replace("Ivan", "Ivanou")
new_fio = f_2
print(new_fio)