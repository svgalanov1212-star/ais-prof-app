import telebot
from telebot import types

TOKEN = '8732203357:AAFihc4vDf2LmUpJ2SsoQn8fuhof9BqBOHk'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message): 
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👤 Мой профиль")
    btn2 = types.KeyboardButton("🔍 Поиск")
    markup.add(btn1, btn2)
    
    welcome_text = (
        "🏗 *Добро пожаловать в АИС.ПРОФ!*

"
        "Это профессиональная платформа для специалистов строительной отрасли.

"
        "Команды:
"
        "/profile - создать профиль
"
        "/search - поиск специалистов
"
        "/vacancies - вакансии
"
        "/pro - PRO-подписка

"
        "Подпишитесь на наш канал: @aisprof_ru"
    )
    bot.send_message(message.chat.id, welcome_text, parse_mode='Markdown', reply_markup=markup)

@bot.message_handler(commands=['profile'])
def profile(message):
    bot.send_message(message.chat.id, "Начнем создание профиля! Пожалуйста, укажите ваше ФИО:")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "👤 Мой профиль":
        bot.send_message(message.chat.id, "Ваш профиль в разработке. Используйте /profile для регистрации.")
    elif message.text == "🔍 Поиск":
        bot.send_message(message.chat.id, "Функция поиска будет доступна после регистрации.")
    else:
        bot.reply_to(message, "Я вас не понимаю. Используйте /help для списка команд.")

bot.polling(none_stop=True)
