v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for v1 in v:
    print(v1 + 1)



str1 = input()
'''for i in range(0, len(str1)):'''
for symbol in str1: 
    print(symbol)


class_scores = [{'school_class': '4a', 'scores': [3,4,4,5,7]}, {'school_class': '4b', 'scores': [3,4,4,5,2, 6]}]
for mass in class_scores:
    summ = 0
    leng = 0
    for score in mass['scores']:
        summ +=score
    leng =len(mass['scores'])
    print(summ/leng)


class_scores = [{'school_class': '4a', 'scores': [3,4,4,5,7]}, {'school_class': '4b', 'scores': [3,4,4,5,2, 6]}]
summ_all = 0
leng_all = 0
for mass in class_scores:
    for score in mass['scores']:
        summ_all +=score
    leng_all +=len(mass['scores'])
print(summ_all/leng_all)

   
