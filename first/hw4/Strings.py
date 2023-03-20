# 1

stroka = 'Тестировщик'


def elem():
    len(stroka)


print(len(stroka))

print(stroka[0])
print(stroka[-1])
print(stroka[2])
print(stroka[-3])

# 2

str_2 = "AutomationPython"
print(len(str_2))
print(str_2[7:16])
print(str_2[0:6] + str_2[10:16])
print(str_2[0:2] + str_2[3:5] + str_2[6:8] + str_2[9:11] + str_2[12:14])
print(str_2[::-1])

# 3

str_3 = "My name is name"
var_list = str_3.split(' ')
var_list.pop(3)
print(' '.join(var_list), "Yegor")

# 4

test_tring = "Hello world!"

print(test_tring.index('w'))
print(test_tring.count('l'))
print(test_tring.startswith('Hello'))
print(test_tring.endswith('qwe'))

