'''v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for v1 in v:
    print(v1 + 1)
str1 = input('Введите что-нибудь: ')
for i in str1[i]:
    print("str1[i]\n")'''

class_scores = [{'school_class': '4a', 'scores': [3,4,4,5,7]}, {'school_class': '4b', 'scores': [3,4,4,5,2, 6]}]
for mass in class_scores:
    summ = 0
    leng = 0
    for score in mass['scores']:
        summ +=score
        leng =len(mass['scores'])
    print(summ/leng)
