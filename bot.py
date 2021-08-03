
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, dispatcher, CallbackQueryHandler

# Defina algunos controladores de comandos. Por lo general, toman los dos argumentos bot y
# actualizar. Los controladores de errores también reciben el objeto TelegramError generado por error.
def start(update: Update, context: CallbackContext):

    boton1 = InlineKeyboardButton(
        text = "Horario para Tramites Documentarios",
        callback_data = '1'
    )
    boton2 = InlineKeyboardButton(
        text = "Datos para contactarce con Secretaria",
        callback_data = '2'
    )
    boton3 = InlineKeyboardButton(
        text = "Requisitos para el Bachillerato",
        callback_data = '3'
    )
    boton4 = InlineKeyboardButton(
        text = "Requisitos para Titulación",
        callback_data = '4'
    )
    """Send a message when the command /start is issued."""
    update.message.reply_text('CIENCIAS DE LA COMPUTACIÓN - UNSA\n\n¡Hola!, \n BIENVENIDO al chat de informacion\n')
    update.message.reply_text(text='¿En que puedo ayudarte?',
        reply_markup= InlineKeyboardMarkup([
            [boton1],
            [boton2],
            [boton3],
            [boton4]
        ])
    )
        
def button(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "1":
        res = horario(query)
    elif query.data == "2":
        res = datos(query)
    elif query.data == "3":
        res = bachi(query)
    elif query.data == "4":
        #res = reboot(query.message.chat_id)
        res = titulo(query)
    else:
        print("nothing to do")

def help(update: Update, context: CallbackContext):
    """Send a message when the command /help is issued."""
    update.message.reply_text('¿Necesitas Ayuda?\n\n Para iniciar de nuevo coloque "/star" y envie el mensaje')

def horario(update: Update):
    update.message.reply_text('HORARIO')
    update.message.reply_photo('https://www.unsa.edu.pe/wp-content/uploads/2021/01/138230780_3625666907509742_8449437901902103612_o.png')
def datos(update: Update):
    update.message.reply_text('-HORARIO DE ATENCION: Lunes-Viernes de 8:45-17:00 HRS \n\n- Encargada: Srta. Raquel \n\n- CORREO: epcc@unsa.edu.pe\n')
def bachi(update: Update):
    update.message.reply_text('REQUISITOS:')
    update.message.reply_photo('https://scontent.faqp2-3.fna.fbcdn.net/v/t1.6435-9/s720x720/151787563_10159091513113529_440347092683463420_n.png?_nc_cat=108&ccb=1-3&_nc_sid=730e14&_nc_eui2=AeGD8rhNQZh3QySw_1xH96-l9CXhv90vX1b0JeG_3S9fVsWyatXnk2WE7bc_8lRP7JnsBgyO4SPCW4mgg-LbXYOU&_nc_ohc=lCI2TajRgnQAX8j8sb5&_nc_ht=scontent.faqp2-3.fna&tp=30&oh=5c78ff90876789d84d66e5af5560c356&oe=60CAA41E')

def titulo(update: Update):
    update.message.reply_text('REQUISITOS:')
    update.message.reply_photo('https://scontent.faqp2-3.fna.fbcdn.net/v/t1.6435-9/s720x720/151787563_10159091513113529_440347092683463420_n.png?_nc_cat=108&ccb=1-3&_nc_sid=730e14&_nc_eui2=AeGD8rhNQZh3QySw_1xH96-l9CXhv90vX1b0JeG_3S9fVsWyatXnk2WE7bc_8lRP7JnsBgyO4SPCW4mgg-LbXYOU&_nc_ohc=lCI2TajRgnQAX8j8sb5&_nc_ht=scontent.faqp2-3.fna&tp=30&oh=5c78ff90876789d84d66e5af5560c356&oe=60CAA41E')


def main():
    """Start the bot."""
    # Crea el actualizador y pásale el token de tu bot.
    # Asegúrese de establecer use_context = True para usar las nuevas devoluciones de llamada basadas en el contexto
    # Publicar la versión 12 esto ya no será necesario
    updater = Updater("TOKEN", use_context=True)
    # Consiga que el despachador registre a los manejadores
    dispatcher = updater.dispatcher 
    # en diferentes comandos - responde en Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button))

    dispatcher.add_handler(CommandHandler("help", help))
    
    # en no comando, es decir, mensaje: haga eco del mensaje en Telegram
    # dp.add_handler(MessageHandler(Filters.text, pizza))


    # Iniciar el bot
    updater.start_polling()

    # Ejecute el bot hasta que presione Ctrl-C o el proceso reciba SIGINT,
    # SIGTERM o SIGABRT. Esto debe usarse la mayor parte del tiempo, ya que
    # start_polling () no bloquea y detendrá el bot con gracia.
    updater.idle()


if __name__ == '__main__':
    main()