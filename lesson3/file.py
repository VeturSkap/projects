with    open('referat.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    print(text)
    text_len = len(text)
    print(text_len)

    words =  text.split()
    words_len = len(words)
    print(words_len)

    new_text = text.replace('.','!')
    print(new_text)

with    open("referat2.txt", "w", encoding="utf-8") as f1:
    f1.writelines(new_text)
