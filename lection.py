# Изменяемые
#list - массив(список) [1,2,3,'Hello',[1,2,3]]
#dict - Словарь {'key':'value',}
#set - Множество (1,2,3,(1,2),[1,2],{...})

#Неизменяемые
#int,float - 1 1,222
#bool - False, True
#string - 'Hello'
#NoneType - None
#tuple - кортеж - (1,2)
#frozenset - неизменяемый set

set_1 = {1,2,3,1,2,3,3}

obj = {'a':1,'b':2}

# for key in obj.values():
#     print(key)

# print(set_1[0])

tuple_1 = (1,2,1,2)
# print(tuple_1[0])

#разница между set и tuple

#1.set - изменяемый, tuple - неизменяемый
#2.set хранит уникальные значения
#3.tuple индексируемый а set - нет


#======================Циклы==================

#1 for

# for x in range(1,4):
    # print('Hello World')




#1. ==

# print(5==5) # сраниваются значения

# print([1,2]==(1,2))

#2. !=

# print(5!=6)

# >, <, >=,<=


# and - И
# or - или
# not - не

# a = 5 > 3 and 4==3 and 5==5 and 3 > 2

# print(a)

# a = 5 > 3 or 4==3 or 4==5

# print(a)

# a = (3 > 5 and 5==5 and 5 > 4) or (3==3)

# print(a)


# Конструкция условия
a = 5
b = 4


if (a == 6):
    print('Зашли в тело первого if')
elif (a % 5 == 1):
    print('Это второй невложенный if')
elif(4 == 4):
    print('!!!!!!!')
elif(...):
    pass
else:
    print('Зашли в тело else')

# for x in range(10):
#     if x == 5:
#         print(x)