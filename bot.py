import logging      # Ayuda a ver lo que sucede con el bot y mostrarlo en consola
import telegram
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram import bot
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters


# Variables
TOKEN = 'TOKEN'

# Configuracion de logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s,"
)
logger = logging.getLogger()

# Funciones para comandos
def start(update, context):
    bot = context.bot
    # chat_Id = update.message.chat_id
    user_Name = update.effective_user["first_name"]
    logger.info(f'El usuario {user_Name} ha iniciado(/start) el bot')   # Consola

    # Lo que se muestra al ejecutar el comando /start
    update.message.reply_text(
        text=f'Bienvenido al Bot 🤖 de la Escuela Profesional de Ciencias de la Computación',
        
    )

def mensaje(update, context):
    bot = context.bot
    updateMsg = getattr(update, 'message', None)
    messageId = updateMsg.message_id #Obtiene el id del mensaje
    chatId = update.message.chat_id
    userName = update.effective_user['first_name']
    text = update.message.text #obtener el texto que envio el usuario en el chat
    logger.info(f'El usuario {userName} ha enviado un nuevo mensaje: "{text}" ;al chat {chatId}')
    # Botones
    btn_contacto = InlineKeyboardButton(
        text='✉️ Contacto de Secretaria',
        callback_data="contacto"
    )
    btn_terminar = InlineKeyboardButton(
        text='Terminar conversación',
        callback_data="terminar"
    )
    btn_tramites = InlineKeyboardButton(
        text='🎓 trámites',
        callback_data="tramite"
    )

    badWord = ['hola','Hola','Buenos','buenos','Buenas','buenas']
    badWord1 = ['consultar','Consultar','Buscando','buscando','Información','información']
    badWord2 = ['Título','título','Titulo','titulo','Bachiller','bachiller','Tramitar','tramitar','Tramites','tramites']
    badWord3 = ['Secretaría','secretaría','Contacto','contacto']
    for i in range(6):
        if badWord[i] in text:
            bot.sendMessage(#se enviara un mensaje al chat
                chat_id = chatId,
                text = f'🤖: ¡Hola! {userName} ☺️, gracias por invocarme, espero que estes muy bien.\n'
                       f'🤖: ¡Dime!, ¿En que puedo ayudarte?'
            )
            break
    for j in range(6):
        if badWord1[j] in text:
            bot.sendMessage(#se enviara un mensaje al chat
                chat_id = chatId,
                text = f'🤖: ¡Bien!, necesitas informacion.\n'
                       f'🤖: {userName},¡dime! : ¿Que tipo de información esta buscando?'
            )
            break
    for k in range(10):  
        if badWord2[k] in text:
            bot.sendMessage(
                chat_id = chatId,
                text = '🤖: perfecto!.\n'
                       '🤖: Elige una de las opciones:',
                reply_markup = InlineKeyboardMarkup([
                    [btn_tramites],
                    [btn_terminar]
                ])
            )
            break
    for l in range(4):
        if badWord3[l] in text:
            bot.sendMessage(
                chat_id = chatId,
                text = '🤖: Bien!.\n'
                       '🤖: Elige una de las opciones:',
                reply_markup = InlineKeyboardMarkup([
                    [btn_contacto],
                    [btn_terminar]
                ])
            )
            break

    
   

def getBotInfo(update, context):
    bot = context.bot
    chat_Id= update.message.chat_id
    user_Name = update.effective_user["first_name"]
    logger.info(f'El usuario {user_Name} ha solicitado información sobre el bot')
    bot.sendMessage(
        chat_id=chat_Id,
        parse_mode="HTML",
        text=f'Hola soy el bot 🤖 de la <b>Escuela Profesional de Ciencia de la Computación - UNSA</b>.'
             f'Si necesitas información sobre trámites de Bachiller y Título Profesional '
             f'puedo ayudarte. Comienza escribiendo /start.' # 2da manera de responder
    )

def terminar_callback_handler(update, context):
    user_Name = update.effective_user["first_name"]
    # print(update.callback_query)
    query = update.callback_query   # Recibe el mensaje
    query.answer()  # Requerido. Responde silenciosamente

    query.edit_message_text(
        parse_mode='HTML',
        text=f' <b>🤖: Lo solicitado ☺️.</b>\n'
             f'🤖: Gracias por escribirme {user_Name}.\n'
             f'🤖: Si hay algo mas en lo que pueda ayudarte, Escribeme...',
    )
    

# Callbacks functions
def contacto_callback_handler(update, context):
    # print(update.callback_query)
    query = update.callback_query   # Recibe el mensaje
    query.answer()  # Requerido. Responde silenciosamente

    query.edit_message_text(
        parse_mode='HTML',
        text=' <b>INFORMACIÓN DE CONTACTO DE LA EPCC</b>\n'
    )
    horario(query,update)
    
def tramites_callback_handler(update, context):
    user_Name = update.effective_user["first_name"]
    logger.info(f'El usuario {user_Name} ha seleccionado Trámites')
    # print(update.callback_query)
    query = update.callback_query   # Recibe el mensaje
    query.answer()  # Requerido. Responde silenciosamente
    query.edit_message_text(
        parse_mode='HTML',
        text=' <b>TRAMITES</b>\n'
    )
    # Botones
    btn_bachiller = InlineKeyboardButton(
        text=' 🎓📃 Trámite para Bachiller',
        callback_data="bachiller"
    )
    btn_titulacion = InlineKeyboardButton(
        text=' ‍🎓📜‍ Trámite para Titulación',
        callback_data="titulacion"
    )

    query.message.reply_text(
        parse_mode='HTML',
        text= f'<b>{user_Name}, estos son los trámites de los que puedo brindarte información 🙂</b> ',
        reply_markup=InlineKeyboardMarkup([
            [btn_bachiller],
            [btn_titulacion]
        ])
    )


def titulacion_callback_handler(update, context):
    # Consola retroalimentación
    user_Name = update.effective_user["first_name"]
    logger.info(f'El usuario {user_Name} ha seleccionado Trámites > Titulacion')

    #Actualizando consulta
    query = update.callback_query  # Recibe el mensaje
    query.answer()  # Requerido. Responde silenciosamente
    query.edit_message_text(
        parse_mode='HTML',
        text='<b> ‍🎓📜‍ Trámite para Titulación</b>'
    )
    query.message.reply_text(
        parse_mode='HTML',
        text='<b>REQUISITOS PARA OBTENER EL TITULO PROFESIONAL</b>\n'
             '▫️Solicitud dirigida al Decano de la facultad en formato UNSA.\n'
             '▫️Recibo de pago de expedito para optar el Título Profesional.\n'
             '▫️Trabajo de investigación digitalizado en formato PDF. \n'
             '▫️Constancia emitida por la Biblioteca Virtual de autorización de publicación en el portal de Tesis '
             'Electrónicas. \n'
             '▫️Certificado negativo de antecedentes penales.\n'
             '▫️Certificado oficial de estudios.\n'
             '▫️Copia legalizada de DNI en formato A5. \n'
             '▫️Copia legalizada del Grado de Bachiller. \n'
             '▫️Fotografía tamaño pasaporte a color fondo blanco. \n'
             '▫️Constancia de Egresado. \n'
             '▫️Constancia que acredite dominio de nivel intermedio de idioma extranjero.\n'
             '▫️Constacia de inscripción a SUNEDU del Grado Académico de Bachiller. \n'
             '▫️Constancia de no adeudar Bienes. \n'
             '▫️Constancia de Biblioteca. \n'
             '▫️Recibo de Subdirección de Finanzas de pago de los derechos por todos los conceptos.\n'
    )
    terminar(query,update)

def bachiller_callback_handler(update, context):
    # Consola retroalimentación
    user_Name = update.effective_user["first_name"]
    logger.info(f'El usuario {user_Name} ha seleccionado Trámites > Bachiller')

    #Actualizando consulta
    query = update.callback_query  # Recibe el mensaje
    query.answer()  # Requerido. Responde silenciosamente

    # Botones
    btn_modo_articulo = InlineKeyboardButton(
        text=' 📃 Modalidad por Artículo de Publicación',
        callback_data="bach_articulo"
    )
    btn_modo_proyecto = InlineKeyboardButton(
        text=' 📃 Modalidad por Trabajo de Investigación',
        callback_data="bach_investigacion"
    )
    query.edit_message_text(
        parse_mode='HTML',
        text='<b> ‍🎓📜‍ Trámite para Bachiller</b>'
    )
    query.message.reply_text(
        parse_mode='HTML',
        text=f'Estas son las dos modalidades para obtener el <b>Grado de Bachiller</b> 👇',
        reply_markup=InlineKeyboardMarkup([
            [btn_modo_articulo],
            [btn_modo_proyecto]
        ])
    )

def bach_articulo_callback_handler(update, context):
    # Consola retroalimentación
    user_Name = update.effective_user["first_name"]
    logger.info(f'El usuario {user_Name} ha seleccionado Trámites > Bachiller > Artículo Científico')

    # Actualizando consulta
    query = update.callback_query  # Recibe el mensaje
    query.answer()  # Requerido. Responde silenciosamente
    query.edit_message_text(
        parse_mode='HTML',
        text='<b> ‍📃 Modalidad por Artículo de Publicación </b>'
    )
    query.message.reply_text(
        parse_mode='HTML',
        text='<b>REQUISITOS PARA OBTENER EL GRADO ACADÉMICO DE BACHILLER</b>\n'
             '<b>MODALIDAD: <em>ARTÍCULO DE PUBLICACIÓN</em></b>\n'
             '▫️Pronto más información de esta modalidad.\n'
    )
    terminar(query,update)

def bach_investigacion_callback_handler(update, context):
    # Consola retroalimentación
    user_Name = update.effective_user["first_name"]
    logger.info(f'El usuario {user_Name} ha seleccionado Trámites > Bachiller > Trabajo de Invetigación')

    # Actualizando consulta
    query = update.callback_query  # Recibe el mensaje
    query.answer()  # Requerido. Responde silenciosamente
    query.edit_message_text(
        parse_mode='HTML',
        text='<b> ‍📃 Modalidad por Trabajo de Investigación </b>'
    )
    query.message.reply_text(
        parse_mode='HTML',
        text='<b>REQUISITOS PARA OBTENER EL GRADO ACADÉMICO DE BACHILLER</b>\n'
             '<b>MODALIDAD: <em>TRABAJO DE INVESTIGACIÓN</em></b>\n'
             '▫️Solicitud dirigida al Decano de la facultad en formato UNSA.\n'
             '▫️Trabajo de investigación digitalizado en formato PDF. \n'
             '▫️Constancia emitida por la Biblioteca Virtual de autorización de publicación en el Repositorio.\n'
             '▫️Certificado negativo de antecedentes penales.\n'
             '▫️Certificado oficial de estudios.\n'
             '▫️Copia legalizada de DNI en formato A5. \n'
             '▫️Fotografía tamaño pasaporte a color fondo blanco. \n'
             '▫️Constancia de Egresado. \n'
             '▫️Constancia que acredite dominio de nivel intermedio de idioma extranjero.\n'
             '▫️Constancia de no adeudar Bienes a la facultad. \n'
             '▫️Constancia de no adeudar material bibliográfico (Dirección general de Biblioteca). \n'
             '▫️Recibo de Subdirección de Finanzas de pago de los derechos por todos los conceptos. \n'
    )
    terminar(query,update)

def horario(update,update1):
    userName = update1.effective_user['first_name']
    
    update.message.reply_text(#se enviara un mensaje al chat
        parse_mode='HTML',
        text=' <b>INFORMACIÓN DE CONTACTO DE LA EPCC</b>\n'
             '▫️Correo electrónico: epcc@unsa.edu.pe\n'
             '▫️Teléfono: 949107364 (Secretaría Raquel)\n'
             '▫️Horario de atención: Lunes a viernes de 8:30 a 10:30AM (vía Meet) \n'
             '▫ Meet de atención: meet.google.com/smh-igaw-vze\n'
    )
    update.message.reply_photo('https://www.unsa.edu.pe/wp-content/uploads/2021/01/138230780_3625666907509742_8449437901902103612_o.png')
    update.message.reply_text(#se enviara un mensaje al chat
        text = f'🤖: Lo solicitado ☺️.\n'
               f'🤖: Gracias por escribirme {userName}.\n'
               f'🤖: Si hay algo mas en lo que pueda ayudarte, Escribeme...\n'
    )

def terminar(update,update1):
    userName = update1.effective_user['first_name']
    update.message.reply_text(#se enviara un mensaje al chat
        text = f'🤖: Lo solicitado ☺️.\n'
               f'🤖: Gracias por escribirme {userName}.\n'
               f'🤖: Si hay algo mas en lo que pueda ayudarte, Escribeme...',
    )


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
    dp.add_handler(CommandHandler("botInfo", getBotInfo))
    dp.add_handler(MessageHandler(Filters.text, mensaje))

    # Crear el callback handler
    dp.add_handler(ConversationHandler(
        entry_points=[
            # Al recibir el patron definido en el data del botón ejecuta la funcion callback
            CallbackQueryHandler(pattern='contacto', callback=contacto_callback_handler),
            CallbackQueryHandler(pattern='terminar', callback=terminar_callback_handler),
            CallbackQueryHandler(pattern='tramite', callback=tramites_callback_handler),
            CallbackQueryHandler(pattern='bachiller', callback=bachiller_callback_handler),
            CallbackQueryHandler(pattern='titulacion', callback=titulacion_callback_handler),
            CallbackQueryHandler(pattern='bach_articulo', callback=bach_articulo_callback_handler),
            CallbackQueryHandler(pattern='bach_investigacion', callback=bach_investigacion_callback_handler)
        ],
        states={},
        fallbacks=[]
    ))

    # Preguntar por mensajes entrantes
    updater.start_polling()

    # Terminar bot con ctrl + c
    updater.idle()