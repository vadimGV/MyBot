import telebot
from keys import keys, TOKEN
from extensions import ConretionException, CryptConveret
bot=telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help (message: telebot.types.Message):
    text= 'Чтобы начать работу введите комманду боту в с ледующем формате :\n ' \
          '<Имя Валюты>\ < В какую валюту перевести> \    <количество переводимой валюты> \ ' \
          'увидеть доступные для перевода валюты /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text='Доступные валюты:'
    for key in keys.keys():
        text='\n'.join((text,key,))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        quot, base, amount = values
        if len(values) != 3:
            raise ConretionException('Слишком много параметров')
        total_base = CryptConveret.convert(quot, base, amount)
        am = float(values[2])
        sum=total_base*am
        text = f'Цена {amount} {quot}, в {base} - {sum}'
        bot.send_message(message.chat.id, text)
    except ConretionException as e:
        bot.reply_to(message, f'Ошибка пользователя\n {e}')
    except Exception as e:
        bot.reply_to(message, f'Неудалось обработать команду \n {e}')


bot.polling()