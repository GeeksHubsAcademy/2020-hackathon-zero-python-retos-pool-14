import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Activar logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Definimos algunas funciones para los comandos. Estos generalmente toman los dos argumentos update y context
def start(update, context):
    """Envia un mensaje cuando se emita el comando /start."""
    logger.info('He recibido un comando /start')
    update.message.reply_text("Hola, Geeks!")
    return "Hola, Geeks!"

def help(update, context):
    """Envia un mensaje cuando se emita el comando /help."""
    logger.info('He recibido un comando /help')
    update.message.reply_text("Ayudame!")
    return "Ayudame!"

def mayus(update, context):
    """Envia un mensaje cuando se emita el comando /mayus."""
    context = context.args
    print(context)
    logger.info('He recibido un comando /mayus')
    update.message.reply_text(context[0].upper())        
    return context[0].upper()

def alreves(update, context):
    """Repite el mensaje del usuario."""
    text = update.message.text
    logger.info('He recibido un comando /alreves')
    update.message.reply_text(text[::-1])        
    return text[::-1]

def error(update, context):
    """Envia los errores por consola"""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Inicio del Bot"""
    #Colocamos el Token creado por FatherBot
    updater = Updater("1299595306:AAE2afydCXqvu_M-H_QUukYut1Fw0rxzIQU", use_context=True)

    # Es el Registro de Comandos a través del dispartcher
    dp = updater.dispatcher

    # Añadimos a la lista de Registro todos los comandos con su función [start - help - mayus]
    #
    #
    #
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('help',help))
    dp.add_handler(CommandHandler('mayus',mayus))
    # Este comando es un Trigger que se lanza cuando no hay comandos [alreves]
    #
    dp.add_handler(MessageHandler(Filters.text,alreves))  
    # Y este espera al error
    dp.add_error_handler(error)

    # Lanzamos el Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
