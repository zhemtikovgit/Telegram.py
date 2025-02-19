import telebot
import requests

# Токен бота (замени на свой)
TOKEN = 'ТОКЕН_ОТ_BotFather'
bot = telebot.TeleBot(TOKEN)

# Функция поиска музыки
def search_music(query):
    url = f"https://api.deezer.com/search?q={query}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['data']:
            track = data['data'][0]
            title = track['title']
            artist = track['artist']['name']
            link = track['link']
            return f"🎵 {title} - {artist}\n🔗 {link}"
    return "Музыка не найдена."

# Команда /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Введи название песни или исполнителя:")

# Обработка сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    query = message.text
    result = search_music(query)
    bot.send_message(message.chat.id, result)

# Запуск бота
bot.polling(none_stop=True)