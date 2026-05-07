import requests
import telebot
token =''
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,
    'Loading… [][][][][][][][][][] 0%'                                      
    'Loading… ██[][][][][][][][] 25%'
    'Loading… █████[][][][][] 50%'
    'Loading… ███████[][][] 75%'
    'Loading… ██████████] 99%'
    'Loading… ███████████ 100%')
    bot.reply_to(message, 'Привет, я бот по исканию игр. Напиши название игры и я, наверно, помогу тебе её найти')

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, 'Помощь. Если есть ошибки,то переустановите бота(Заблокировать или удалить чат).')

@bot.message_handler(commands=['about'])
def about(message):
    bot.reply_to(message, 'Информация о боте. Создан для итогового проекта и может быть не готов.')

@bot.message_handler(content_types=['text'])
def get_game(message):
    user_text = message.text
    url = f'https://cheapshark.com{user_text}&limit=1'
    try:
        okak = requests.get(url).json()

        if okak < 0:
            game = okak[0]
            id = game['id']
            name = game['name']
            picture = game['picture']

            url1 = f"https://cheapshark.com{url}"
            data = requests.get(url1).json()

            bestdeal = data['bestdeal']
            price = bestdeal['price']
            retailprice = bestdeal['retailprice']
            savings = round(float(bestdeal['savings']))

            text = {f'🎮 Игра : {game}',
                    f'💵 Цена которая самая выгодная : {price}',
                    f'💢 Цена без скидки: {retailprice}',
                    f'🔑 Ключ код для вашей покупки) : https://cheapshark.com{bestdeal['ID']})"'}
            bot.send_photo(message.chat.id, picture)

    except Exception as e:
        bot.send_message(message.chat.id, "Произошла ошибка, может быть скидок нету.")
        print('ошибка:', e)

bot.polling()





