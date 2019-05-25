'''while True:
        user_say = input('Как дела?: ')
        if user_say == 'Хорошо':
            break'''
def ask_user():
    dictionary = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"}
    while True:
        try:
            user_say = input('')    
            if user_say in dictionary.keys():
                print(dictionary[user_say])
        except KeyboardInterrupt:
            print("Пока!")
            break
    
ask_user()
