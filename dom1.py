a = "Hello"
b = "World"
c = a + b
print(c)

a = 'hello wworld'
print(len(a))


a = 'HELLO WORLD'
b = 'hello world'
c = 'hello world'
print(a.isupper())
print(b.islower())
print(c.title())


a = 'Hello World'            
print(a[::-1])


a = 'Hello World'
print(a == a[::-1])


a = 'Hello World'
b = a.find('2' 'o')
print(b)


a = 'Hello World'
b = a.replace(' ','_')
print(b)


a = 'hello'
b = 'world'
if 'a' in 'b':
    print("второя строка содержится в первой строке.")
else:
    print("второя строка не содержится в первой строке")


task = "задание работа дело"
print(task)
print(task.split())

a = ['Hello','world','work']
b = ",".join(a)
print(b)