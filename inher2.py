#==================Наследование=============

# Наследование - принцип ООП, в котором мы можем наследовать, переопределять и использовать 
# в дочернем классе все атрибуты и методы родительского класса

# class A:

#     attr = 'Hello'
    
#     def method_a(self):
#         print('Это метод класса A')


# class B(A):
    
#     def method_b(self):
#         print('Это метод класса B')


# c = C()

# c.method_a()
# c.method_b()


# b = B()

# b.method_a()

# print(b.attr)



#=============Виды наследований===========

#1. Одиночное наследование (когда мы наследуемся от 1 класса)
#2. Множественное наследование (когда мы наследуемся от 2 и более классов)
#3. Многоуровневое наследование
#4. Иерархическое наследование (когда от одного класса много дочерних)
#5. Гибридное наследование (все смешано)

# Проблема MRO (Method Resolution Order)

# class A:
#     pass
#     # def __str__(self) -> str:
#     #     return 'A'
    
# class B(A):
#     pass

#     # def __str__(self) -> str:
#     #     return 'B'

# class C(A):
#     pass

# class D(B,C):
#     pass

# Проблема перекрестного наследования


class A:
    pass

class B:
    pass

class D(A,B):
    pass

class E(A,B):
    pass

class F(D,E):
    def __init__(self,a) -> None:
        self.a = a
        print('Сработал магический метод __init__')

    # def __eq__(self, value: object) -> bool:
    #     return super().__eq__(value)


    def c(self):
        return 'c'

f = F('name')






