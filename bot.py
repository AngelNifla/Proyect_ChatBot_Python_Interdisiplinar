# BOT TELEGRAM : CONSULTAS EPCC
# -------------------------------
# Implementación de Lectura de Base de datos

import logging  # Ayuda a ver lo que sucede con el bot y mostrarlo en consola

import telegram
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters

import botDB

# Variables
TOKEN = '1862455246:AAHDE6lLYMHHYk7-p_rBSgf_L3CYRkO4IYA'

# Configuracion de logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s,"
)
logger = logging.getLogger()

# Funciones para comandos
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

# # Botones para start
btn_contacto = InlineKeyboardButton(
    text='✉️ Contacto de EPCC',
    callback_data="contacto"
)
btn_tramites = InlineKeyboardButton(
    text='🎓 Información de trámites',
    callback_data="tramite"
)
btn_terminar = InlineKeyboardButton(
    text='Terminar conversación',
    callback_data="terminar"
)

def start(update, context):
    bot = context.bot
    # chat_Id = update.message.chat_id
    user_Name = update.effective_user["first_name"]
    logger.info(f'El usuario {user_Name} ha iniciado(/start) el bot')   # Consola retroalimentación

    # Lo que se muestra al ejecutar el comando /start
    update.message.reply_text(
        text=f'Hola {user_Name} ☺️.Gracias por usar nuestro bot.\n'
             f'🤖: A continuación te mostraré los tipos de información que puedo brindarte. '
             f'Sólo toca la opción que te interesa:',
        reply_markup=InlineKeyboardMarkup([
            [btn_contacto],
            [btn_tramites]
        ])
    )

# Mensaje para la conversación
# ----------------------------
def mensaje(update, context):
    bot = context.bot
    updateMsg = getattr(update, 'message', None)
    messageId = updateMsg.message_id  # Obtiene el id del mensaje
    chatId = update.message.chat_id
    userName = update.effective_user['first_name']
    text = update.message.text  # obtener el texto que envio el usuario en el chat
    logger.info(f'El usuario {userName} ha enviado un nuevo mensaje: "{text}" ;al chat {chatId}')

    # Key words
    badWord = ['hola', 'Hola', 'Buenos', 'buenos', 'Buenas', 'buenas']
    badWord1 = ['consultar', 'Consultar', 'Buscando', 'buscando', 'Información', 'información', 'informacion',
                'Informacion']
    badWord2 = ['Título', 'título', 'Titulo', 'titulo', 'Bachiller', 'bachiller', 'Tramitar', 'tramitar', 'Tramites',
                'tramites', 'trámites', 'Trámites']
    badWord3 = ['Secretaría', 'secretaría', 'Contacto', 'contacto', 'escuela']
    for i in range(6):
        if badWord[i] in text:
            bot.sendMessage(  # se enviara un mensaje al chat
                chat_id=chatId,
                text=f'🤖: ¡Hola {userName}! ☺️, gracias por invocarme, espero que estes muy bien. '
                     f' ¿En qué puedo ayudarte?'
            )
            break
    for j in range(6):
        if badWord1[j] in text:
            bot.sendMessage(  # se enviara un mensaje al chat
                chat_id=chatId,
                text=f'🤖: ¡Bien!, necesitas información.\n'
                     f'🤖: {userName},¡Dime! : ¿Que tipo de información esta buscando?'
            )
            break
    for k in range(10):
        if badWord2[k] in text:
            bot.sendMessage(
                chat_id=chatId,
                text='🤖: ¡Perfecto!\n'
                     '🤖: Elige una de las opciones:',
                reply_markup=InlineKeyboardMarkup([
                    [btn_bachiller],
                    [btn_titulacion],
                    [btn_terminar]
                ])
            )
            break
    for l in range(4):
        if badWord3[l] in text:
            bot.sendMessage(
                chat_id=chatId,
                text='🤖: Bien!.\n'
                     '🤖: Elige una de las opciones:',
                reply_markup=InlineKeyboardMarkup([
                    [btn_contacto],
                    [btn_terminar]
                ])
            )
            break
            
def bot_feedback(update, context):
    # update.message.reply_photo(
    #     'https://drive.google.com/file/d/1aXFhaBXeS3DpxB10KmJx13m645V4mWrl/view?usp=sharing')
    # update.message.reply_text(  # se enviara un mensaje al chat
    #     parse_mode='HTML',
    #     text=' <b>INFORMACIÓN DE CONTACTO DE LA EPCC</b>\n'
    #          '▫️Correo electrónico: epcc@unsa.edu.pe\n'
    #          '▫️Teléfono: 949107364 (Secretaría Raquel)\n'
    #          '▫️Horario de atención: Lunes a viernes de 8:30 a 10:30AM (vía Meet) \n'
    #          '▫ Meet de atención: meet.google.com/smh-igaw-vze\n'
    # )
    update.message.reply_text(  # se enviara un mensaje al chat
        text=f'🤖: Aquí tienes lo solicitado ☺️.\n'
             f'🤖: Si hay algo mas en lo que pueda ayudarte, escríbeme...\n'
    )

# Funciones auxiliares para la conversación
def terminar(update, update1):
    userName = update1.effective_user['first_name']
    update.message.reply_text(  # se enviara un mensaje al chat
        text=f'🤖: Lo solicitado ☺️.\n'
             f'🤖: Gracias por escribirme {userName}.\n'
             f'🤖: Si hay algo mas en lo que pueda ayudarte, Escribeme...',
    )


# Botones para callbacks de tramites
# ----------------------------------
btn_bachiller = InlineKeyboardButton(
    text=' 🎓📃 Trámite para Bachiller',
    callback_data="bachiller"
)
btn_titulacion = InlineKeyboardButton(
    text=' ‍🎓📜‍ Trámite para Titulación',
    callback_data="titulacion"
)

# Callbacks functions
# -------------------

# Obtener informacion de BD y construcción de string
list_info_contacto = botDB.select_list_info(0)
string_contacto =''
for row in list_info_contacto:
    if isinstance(row, dict):
        string_contacto += '▫️<b>' + row['Tipo Informacion'] + ':</b> ' + row['Información'] + '\n'

req_bach_automatico = botDB.select_list_info(1)
string_bach_automatico =''
for row in req_bach_automatico:
    if isinstance(row, dict):
        string_bach_automatico += '▫️<b>' + str(row['Id']) + '.</b> ' + row['Requisito'] + '\n'

req_bach_ti = botDB.select_list_info(2)
string_bach_ti =''
for row in req_bach_ti:
    if isinstance(row, dict):
        string_bach_ti += '▫️<b>' + str(row['Id']) + '.</b> ' + row['Requisito'] + '\n'

req_titulo_ti = botDB.select_list_info(3)
string_titulo_ti =''
for row in req_titulo_ti:
    if isinstance(row, dict):
        string_titulo_ti += '▫️<b>' + str(row['Id']) + '.</b> ' + row['Requisito'] + '\n'

req_titulo_suficiencia = botDB.select_list_info(4)
string_titulo_suficiencia =''
for row in req_titulo_suficiencia:
    if isinstance(row, dict):
        string_titulo_suficiencia += '▫️<b>' + str(row['Id']) + '.</b> ' + row['Requisito'] + '\n'

def contacto_callback_handler(update, context):
    user_Name = update.effective_user["first_name"]
    query = update.callback_query   # Recibe el mensaje
    query.answer()  # Requerido. Responde silenciosamente
    logger.info(f'El usuario {user_Name} ha solicitado información de Contacto')

    query.edit_message_text(
        parse_mode='HTML',
        text=' <b>INFORMACIÓN DE CONTACTO DE LA EPCC</b>\n' + string_contacto,
    )
    bot_feedback(query, update)

def tramites_callback_handler(update, context):
    # Consola retroalimentación
    user_Name = update.effective_user["first_name"]
    logger.info(f'El usuario {user_Name} ha seleccionado Trámites')

    #Actualizando consulta
    query = update.callback_query  # Recibe el mensaje
    query.answer()  # Requerido. Responde silenciosamente

    query.edit_message_text(
        parse_mode='HTML',
        text=f'🤖: {user_Name}, estos son los trámites de los que puedo brindarte información 🙂 ',
        reply_markup=InlineKeyboardMarkup([
            [btn_bachiller],
            [btn_titulacion]
        ])
    )

def bachiller_callback_handler(update, context):
    # Consola retroalimentación
    user_Name = update.effective_user["first_name"]
    logger.info(f'El usuario {user_Name} ha seleccionado Trámites > Bachiller')

    #Actualizando consulta
    query = update.callback_query  # Recibe el mensaje
    query.answer()  # Requerido. Responde silenciosamente

    # Botones
    btn_modo_articulo = InlineKeyboardButton(
        text=' 📃 Modalidad Bachiller Automático - 2021',
        callback_data="bach_automatico"
    )
    btn_modo_proyecto = InlineKeyboardButton(
        text=' 📃 Modalidad por Trabajo de Investigación',
        callback_data="bach_investigacion"
    )
    btn_back = InlineKeyboardButton(
        text=' ⬅️Atrás',
        callback_data="tramite"
    )

    query.edit_message_text(
        parse_mode='HTML',
        text=f'🤖: Estas son las dos modalidades para obtener el <b>Grado de Bachiller</b> 👇',
        reply_markup=InlineKeyboardMarkup([
            [btn_modo_articulo],
            [btn_modo_proyecto],
            [btn_back]
        ])
    )

def bach_automatico_callback_handler(update, context):
    # Consola retroalimentación
    user_Name = update.effective_user["first_name"]
    logger.info(f'El usuario {user_Name} ha seleccionado Trámites > Bachiller > Artículo Científico')
    btn_back = InlineKeyboardButton(
        text=' ⬅️Atrás',
        callback_data="bachiller"
    )
    # Actualizando consulta
    query = update.callback_query  # Recibe el mensaje
    query.answer()  # Requerido. Responde silenciosamente

    query.edit_message_text(
        parse_mode='HTML',
        text='<b>REQUISITOS PARA OBTENER EL GRADO ACADÉMICO DE BACHILLER</b>\n' 
             '<b>MODALIDAD: <em>BACHILLER AUTOMÁTICO 2021</em></b>\n' + string_bach_automatico,
        reply_markup=InlineKeyboardMarkup([
            [btn_back]
        ])
    )
    terminar(query, update)

def bach_investigacion_callback_handler(update, context):
    # Consola retroalimentación
    user_Name = update.effective_user["first_name"]
    logger.info(f'El usuario {user_Name} ha seleccionado Trámites > Bachiller > Trabajo de Invetigación')
    # button
    btn_back = InlineKeyboardButton(
        text=' ⬅️Atrás',
        callback_data="bachiller"
    )
    # Actualizando consulta
    query = update.callback_query  # Recibe el mensaje
    query.answer()  # Requerido. Responde silenciosamente

    query.edit_message_text(
        parse_mode='HTML',
        text='<b>REQUISITOS PARA OBTENER EL GRADO ACADÉMICO DE BACHILLER</b>\n'
             '<b>MODALIDAD: <em>TRABAJO DE INVESTIGACIÓN</em></b>\n' + string_bach_ti,
        reply_markup=InlineKeyboardMarkup([
            [btn_back]
        ])
    )
    terminar(query, update)

def titulacion_callback_handler(update, context):
    # Consola retroalimentación
    user_Name = update.effective_user["first_name"]
    logger.info(f'El usuario {user_Name} ha seleccionado Trámites > Titulacion')
    # boton
    btn_back = InlineKeyboardButton(
        text=' ⬅️Atrás',
        callback_data="tramite"
    )
    #Actualizando consulta
    query = update.callback_query  # Recibe el mensaje
    query.answer()  # Requerido. Responde silenciosamente

    query.edit_message_text(
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
             '▫️Recibo de Subdirección de Finanzas de pago de los derechos por todos los conceptos.\n',
        reply_markup=InlineKeyboardMarkup([
            [btn_back]
        ])
    )
    terminar(query, update)

def terminar_callback_handler(update, context):
    user_Name = update.effective_user["first_name"]
    query = update.callback_query   # Recibe el mensaje
    query.answer()  # Requerido. Responde silenciosamente

    query.edit_message_text(
        parse_mode='HTML',
        text=f' <b>🤖: Aqui tienes lo solicitado ☺️.</b>\n'
             f'🤖: Si hay algo mas en lo que pueda ayudarte, escríbeme...',
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
            CallbackQueryHandler(pattern='terminar', callback=terminar_callback_handler) #Terminar conversación
        ],
        states={},
        fallbacks=[]
    ))

    # Preguntar por mensajes entrantes to do el tiempo
    updater.start_polling()

    # Terminar bot con ctrl + c
    updater.idle()