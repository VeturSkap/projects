def strings(s1, s2):
    if isinstance(s1, str) == False or isinstance(s2, str) == False:
        return 0
    if s1 == s2:
        return 1
    if s1 != s2:
        if len(s1) > len(s2):
            return 2
        if s2 == 'learn':
            return 3
def main():
    x = '3243'
    y = 'cdkjdskjdsjds'
    print(strings(x, y))
    a = 'ffjffjgf'
    b = 'learn'
    print(strings(a, b))
    c = 1645
    d = 'jfhkjrhfgf'
    print(strings(c, d))
main()