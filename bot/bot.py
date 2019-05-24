from telegram.ext import Updater, CommandHandler

def greet_user(bot, update):
    print('Вызван /start')
    update.message.reply_text('Я бот')

def main():
    PROXY = {'proxy_url': 'socks5://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

    mybot = Updater("899496990:AAEaUH5wiOYsTf-pbY2PcT8IY7qyBNGL5UQ", request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))

    mybot.start_polling()
    mybot.idle()
    
main()