# BOT TELEGRAM : CONSULTAS EPCC
# -------------------------------
# Implementación de Lectura de Base de datos

import logging  # Ayuda a ver lo que sucede con el bot y mostrarlo en consola

import telegram
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters
from funcion import *
from Bnts import *

# Variables
TOKEN = '1877045379:AAG0C4L_WQp0F-otZPJg0yevDNiavBhvFp0'

# Configuracion de logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s,"
)
logger = logging.getLogger()

# Funciones para comandos
#-----------------------------------------------
def getBotInfo(update, context):
    bot = context.bot
    chat_Id= update.message.chat_id
    user_Name = update.effective_user["first_name"]
    logger.info(f'El usuario {user_Name} ha solicitado información(/infoBot) sobre el bot')

    bot.sendMessage(
        chat_id=chat_Id,
        parse_mode="HTML",
        text=f'Hola soy el bot 🤖 de la <b>Escuela Profesional de Ciencia de la Computación - UNSA</b>.'
             f'Si necesitas información sobre trámites de Bachiller y Título Profesional '
             f'puedo ayudarte. Comienza escribiendo /start. \n' 
             f'También puedes escribirme en el chat y trataré de mostrarte la información más adecuada.'  # 2da manera de responder
    )


#Funcion cuando se utilize el comando "/start"
#-----------------------------------------------
def start(update, context):
    bot = context.bot
    # chat_Id = update.message.chat_id
    user_Name = update.effective_user["first_name"]
    logger.info(f'El usuario {user_Name} ha iniciado(/start) el bot')   # Consola retroalimentación

    # Lo que se muestra al ejecutar el comando /start
    update.message.reply_text(
        parse_mode='HTML',
        text=' <b>BIENVENIDO AL CHATBOT DE CIENCIAS DE LA COMPUTACIÓN</b>\n',
        #text=f'Hola {user_Name} ☺️.Gracias por usar nuestro bot.\n'
        #     f'🤖: A continuación te mostraré los tipos de información que puedo brindarte. '
        #     f'Sólo toca la opción que te interesa:',
        #reply_markup=InlineKeyboardMarkup([
        #    [btn_contacto],
        #    [btn_tramites]
        #])
    )


# Funcion que recibe los mensajes del usuario
# -----------------------------------------
def mensaje(update, context):
    bot = context.bot
    updateMsg = getattr(update, 'message', None)
    messageId = updateMsg.message_id  # Obtiene el id del mensaje
    chatId = update.message.chat_id
    userName = update.effective_user['first_name']
    text = update.message.text  # obtener el texto que envio el usuario en el chat
    logger.info(f'El usuario {userName} ha enviado un nuevo mensaje: "{text}" ;al chat {chatId}')
    palabras = text.split()

    if verificar(palabras)==1:
        hola(update,context)
    
    if verificar(palabras)==2:
        hola_uni(update,context)
        tramites(update,context)

    if verificar(palabras)==3:
        hola_uni(update,context)
        bachiller(update,context)

    if verificar(palabras)==4:
        hola_uni(update,context)
        titulo_investigacion(update,context)
        solicitud_confir(update, context)

    if verificar(palabras)==5:
        hola_uni(update,context)
        contac(update,context)
        solicitud_confir(update,context)

    if verificar(palabras)==6:
        tramites(update,context)

    if verificar(palabras)==7:
        bachiller(update,context)

    if verificar(palabras)==8:
        titulo_investigacion(update,context)
        solicitud_confir(update,context)

    if verificar(palabras)==9:
        contac(update,context)
        solicitud_confir(update,context)

    if verificar(palabras)==10:
        fin(update,context)
    
    if verificar(palabras)==11:
        consultas_noespecifico(update,context)

    if verificar(palabras)==12:
        hola_uni(update,context)
        bachiller_investigacion(update,context)
    
    if verificar(palabras)==13:
        hola_uni(update,context)
        bachiller_automatico(update,context)
    
    if verificar(palabras)==14:
        hola_uni(update,context)
        titulo_investigacion(update,context)
    
    if verificar(palabras)==15:
        hola_uni(update,context)
        titulo_suficiencia(update,context)
    
    if verificar(palabras)==16:
        bachiller_investigacion(update,context)
    
    if verificar(palabras)==17:
        bachiller_automatico(update,context)
    
    if verificar(palabras)==18:
        titulo_investigacion(update,context)
    
    if verificar(palabras)==19:
        titulo_suficiencia(update,context)

    if verificar(palabras)==20:
        titulo(update,context)
        

# Main Function
if __name__ == '__main__':
    mybot = telegram.Bot(token=TOKEN)
    print(mybot.getMe())  # Muestra en consola información sobre el bot

    # Updater: se conecta y recibe los mensajes
    updater = Updater(mybot.token, use_context=True)

    # Crear el 'despachador'
    dp = updater.dispatcher

    # Crear comando y el método (acción del comando)
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("info", getBotInfo))
    dp.add_handler(MessageHandler(Filters.text, mensaje))   # Maneja las key words para la conversación

    # Crear el callback handler
    # ConversationHandler define como será la conversación
    dp.add_handler(ConversationHandler(
        entry_points=[
            # Al recibir el patron definido en el data del botón ejecuta la funcion callback
            CallbackQueryHandler(pattern='contacto', callback=contacto_callback_handler),
            CallbackQueryHandler(pattern='tramite', callback=tramites_callback_handler),
            CallbackQueryHandler(pattern='bachiller', callback=bachiller_callback_handler),
            CallbackQueryHandler(pattern='titulacion', callback=titulacion_callback_handler),
            CallbackQueryHandler(pattern='bach_automatico', callback=bach_automatico_callback_handler),
            CallbackQueryHandler(pattern='bach_investigacion', callback=bach_investigacion_callback_handler),
            CallbackQueryHandler(pattern='titul_suficiencia', callback=titul_suficiencia_callback_handler),
            CallbackQueryHandler(pattern='titul_investigacion', callback=titul_investigacion_callback_handler),
            CallbackQueryHandler(pattern='terminar', callback=terminar_callback_handler) #Terminar conversación
        ],
        states={},
        fallbacks=[]
    ))

    # Preguntar por mensajes entrantes to do el tiempo
    updater.start_polling()

    # Terminar bot con ctrl + c
    updater.idle()