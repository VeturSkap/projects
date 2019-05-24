def get_summ(one, two, delimiter='&'):
    return one+delimiter+two

text=get_summ('Learn', 'python')
print(text)
text1=get_summ('Learn', 'python').upper()
print(text1)
