def get_summ(num_one, num_two):
    try:
        summ = int(num_one)+int(num_two)
        return summ
    except ValueError:
        return "Приведение типов не сработало"


x = 'fdsjjds'
y = 15
print(get_summ(x, y))