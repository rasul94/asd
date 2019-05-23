
import telebot


bot = telebot.TeleBot('865347255:AAGRAO9ONrwdU4xpgo6RZrgbCITAMdHzz6o')

@bot.message_handler(content_types=['text'])
def hadle_text(message):
    if message.text == 'text':
        bot.send_message(message.from_user.id, "ishladi")
    else:
        bot.send_message(message.from_user.id, "salom")
        
bot.polling(none_stop=True, interval=0)