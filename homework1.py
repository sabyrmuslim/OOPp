# создание и печать строки:

a = "Hello World"
print(a)
 
# длина строки:

a = 'kyrgyzstan'
print(len(a))

# изменение регистра:

a = 'HELLO WORLD'
b = 'hello world'
c = 'hello world'
print(a.isupper())
print(b.islower())
print(c.title())

# обратная строка:

a = 'Hello World'            
print(a[::-1])

# проверка полиндрома:

a = 'kazak'
print(a == a[::-1])

# подсчет символов:

a = 'Hello World'
b = a.find('l')
print(b)

# замена символов:

a = 'Hello World'
b = a.replace(' ','_')
print(b)

# проверка наличия подстроки:

a = 'hello'
b = 'world'
if 'a' in 'b':
    print("второя строка содержится в первой строке.")
else:
    print("второя строка не содержится в первой строке")

# разделение строки:

y = "red blue green"
print(y)
print(y.split())

# соединение списка строк:

x = ["Hello","world","work"]
b = ','.join(x)
print(b)