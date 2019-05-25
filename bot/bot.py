from telegram.ext import Updater, CommandHandler
import ephem
def greet_user(bot, update):
    print('Вызван /start')
    update.message.reply_text('Я бот')

def planets(bot, update):
    print('Вызван /planet')
    print(update.message.text.split( ))
    name_planet=update.message.text.split( )
    all_planet = {"Mars": ephem.Mars, "Saturn": ephem.Saturn, "Mercury": ephem.Mercury, "Venus": ephem.Venus, "Jupiter": ephem.Jupiter}
    if name_planet[1] in all_planet:
        print(ephem.constellation(all_planet[name_planet[1]](ephem.now())))

def main():
    PROXY = {'proxy_url': 'socks5://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

    mybot = Updater("899496990:AAEaUH5wiOYsTf-pbY2PcT8IY7qyBNGL5UQ", request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planets))

    mybot.start_polling()
    mybot.idle()
    
main()