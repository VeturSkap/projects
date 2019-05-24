'''a=2
b=2.5-a
print(a+b)
name ='Люба'
b = 'Привет {user}!'.format(user=name)
print(b)

v=input('Введите число от 1 до 10: ')
print(f'{v}')
dec=int(input('Введите число от 1 до 10: '))
dec2=dec+10
print(dec2)

name=input('Введите ваше имя: ')
d=name.capitalize()
print('Привет,', d)
g=name.upper()
print('Привет, ', g, '! Как дела?', sep='')
print(float('1'))
print(int(float('2.5')))
print(bool(1))
print(bool(''))
print(bool(0))
num=[3, 5, 7, 9, 10.5]
print(num)
num=[3, 5, 7, 9, 10.5]
num.append("Python")
print(len(num))
num[0]
print(num[0])
num[5]
print(num[5])
num[1:4]
print(num[1:4])
del num[5]
print(num)'''

voc = {"city": "Москва", "temperature": "20"}
'''print(voc["city"])
voc["temperature"]=int(voc["temperature"])-5
print(voc["temperature"])
print(voc)

print(voc["country"])'''
voc.get("country", "Россия")
voc["date"] = "27.05.2019"
print(len(voc))