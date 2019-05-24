age = int(input("Введите Ваш возраст: "))
if age < 6:
    print('Детсад')
elif age < 18:
    print('Школа')
elif age < 23:
    print('ВУЗ')
else:
    print('Работа')