# В ООП есть 5 принципов

# 1. Инкапсуляция
# 2. Наследование
# 3. Полиморфизм
# 4. Ассоциация
# 5. Абстракция

#=============Инкапсуляция=========

# Инкапсуляция - 1. Сбор всех атрибутов в одну капсулу(класс)
#                2. Сокрытие данных

# Виды сокрытия данных

# 1. public - открытый (name)
# 2. protected - защищенный (_name)
# 3. private - приватный (__name)

class A:
    a = 'public'
    _b = 'protected'
    __c = 'private'

    def get_attr3(self):
        return A.__attr3

    def set_attr3(self,new_value):
        A.__attr3 = new_value

a = A()
# print(a._attr2)

class B(A):
    pass

b = B()

# print(b._attr2)






# a = A()

# print(A._A__attr3)
# print(a.get_attr3())
# a.set_attr3('Hello world')
# print(a.get_attr3())


# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age

#     def get_age(self):
#         return self.__age
    
#     def set_age(self,new_value):
#         if new_value > 0 and new_value < 120:
#             self.__age = new_value
#         else:
#             raise Exception('Такого возраста не может быть')


    
# maxim = Person('Maxim',22)
# print(maxim.get_age())

# maxim.set_age(23)

# print(maxim.get_age())


class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age
    
    @age.getter
    def age(self):
        print('Вы вызвали метод getter для age')
        return self.__age

    @age.setter
    def age(self,new_value):
        # print('Сработал метод age.setter')
        # if new_value > 0 and new_value < 120:
        #     self.__age = new_value
        # else:
        #     raise Exception('Такого возраста не может быть')
        self.__age = new_value


maxim = Person('Maxim',22)
print(maxim.age)
maxim.age = -100
print(maxim.age)

    






        








# a = A('Ascar')
# a.my_attr = 'Hello'
# print(a.__dict__) # Выводит все атрибуты обьекта





