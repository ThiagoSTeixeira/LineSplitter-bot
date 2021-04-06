from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

updater = Updater(token = 'INSERT-TOKEN', use_context = True)
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Salve meim, lansa a braba pro pai cortar")                

    
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

    
def split(update, context):
    links = update.message.text.split('\n')
    for l in links:
        context.bot.send_message(chat_id = update.effective_chat.id, text = l)

split_handler = MessageHandler(Filters.text & (~Filters.command), split)
dispatcher.add_handler(split_handler)

updater.start_polling()
