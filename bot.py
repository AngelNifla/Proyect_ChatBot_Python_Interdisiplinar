# BOT TELEGRAM : CONSULTAS EPCC
#-------------------------------
# Implementación de diálogo


import logging      # Ayuda a ver lo que sucede con el bot y mostrarlo en consola
import telegram
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters
from funcion import  bachi, consultas_noespecifico, fin, titul, verificar, contac, hola, hola_uni
# Variables
TOKEN = 'TOKEN'

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

# # Botones
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

# Botones
btn_modo_articulo = InlineKeyboardButton(
        text=' 📃 Modalidad por Artículo de Publicación',
        callback_data="bach_articulo"
    )
btn_modo_proyecto = InlineKeyboardButton(
        text=' 📃 Modalidad por Trabajo de Investigación',
        callback_data="bach_investigacion"
    )
btn_back = InlineKeyboardButton(
        text=' ⬅️Atrás',
        callback_data="tramite"
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

# Mensaje maneja la conversación con el bot
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

    if verificar(palabras)==3:
        hola_uni(update,context)
        bot.sendMessage(
            chat_id=chatId,
            parse_mode='HTML',
            text=f'🤖: Estas son las dos modalidades para obtener el <b>Grado de Bachiller</b> 👇',
            reply_markup=InlineKeyboardMarkup([
                [btn_modo_articulo],
                [btn_modo_proyecto],
                ])
            )

    if verificar(palabras)==4:
        hola_uni(update,context)
        titul(update,context)

    if verificar(palabras)==5:
        hola_uni(update,context)
        contac(update,context)

    if verificar(palabras)==6:
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

    if verificar(palabras)==7:
       bachi(update,context)
       bot.sendMessage(
            chat_id=chatId,
            parse_mode='HTML',
            text=f'🤖: Estas son las dos modalidades para obtener el <b>Grado de Bachiller</b> 👇',
            reply_markup=InlineKeyboardMarkup([
                [btn_modo_articulo],
                [btn_modo_proyecto],
                ])
            )

    if verificar(palabras)==8:
       titul(update,context)

    if verificar(palabras)==9:
        contac(update,context)

    if verificar(palabras)==10:
        fin(update,context)
    
    if verificar(palabras)==11:
        consultas_noespecifico(update,context)

# Callbacks functions
# -------------------
def contacto_callback_handler(update, context):
    user_Name = update.effective_user["first_name"]
    query = update.callback_query   # Recibe el mensaje
    query.answer()  # Requerido. Responde silenciosamente
    logger.info(f'El usuario {user_Name} ha solicitado información de Contacto')

    query.edit_message_text(
        parse_mode='HTML',
        text=' <b>INFORMACIÓN DE CONTACTO DE LA EPCC</b>\n'
             '▫️Correo electrónico: epcc@unsa.edu.pe\n'
             '▫️Teléfono: 949107364 (Secretaría Raquel)\n'
             '▫️Horario de atención: Lunes a viernes de 8:30 a 10:30AM (vía Meet) \n'
             '▫ Meet de atención: meet.google.com/smh-igaw-vze\n'
    )
    bot_feedback(query, update)

## bot feedback
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

## botones de tramites

btn_bachiller = InlineKeyboardButton(
    text=' 🎓📃 Trámite para Bachiller',
    callback_data="bachiller"
)
btn_titulacion = InlineKeyboardButton(
    text=' ‍🎓📜‍ Trámite para Titulación',
    callback_data="titulacion"
)


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



def bachiller_callback_handler(update, context):
    # Consola retroalimentación
    user_Name = update.effective_user["first_name"]
    logger.info(f'El usuario {user_Name} ha seleccionado Trámites > Bachiller')

    #Actualizando consulta
    query = update.callback_query  # Recibe el mensaje
    query.answer()  # Requerido. Responde silenciosamente

    

    query.edit_message_text(
        parse_mode='HTML',
        text=f'🤖: Estas son las dos modalidades para obtener el <b>Grado de Bachiller</b> 👇',
        reply_markup=InlineKeyboardMarkup([
            [btn_modo_articulo],
            [btn_modo_proyecto],
            [btn_back]
        ])
    )


def bach_articulo_callback_handler(update, context):
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
             '<b>MODALIDAD: <em>ARTÍCULO DE PUBLICACIÓN</em></b>\n'
             '▫️Pronto más información de esta modalidad.\n',
        reply_markup=InlineKeyboardMarkup([
            [btn_back]
        ])
    )


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
             '▫️Recibo de Subdirección de Finanzas de pago de los derechos por todos los conceptos. \n',
        reply_markup=InlineKeyboardMarkup([
            [btn_back]
        ])
    )


def terminar_callback_handler(update, context):
    user_Name = update.effective_user["first_name"]
    query = update.callback_query   # Recibe el mensaje
    query.answer()  # Requerido. Responde silenciosamente

    query.edit_message_text(
        parse_mode='HTML',
        text=f'🤖: ESPERO HABERTE AYUDADO ☺️.\n'
    )


# Funciones auxiliares para la conversación

def terminar(update, update1):
    userName = update1.effective_user['first_name']
    update.message.reply_text(  # se enviara un mensaje al chat
        parse_mode='HTML',
        text=f'🤖: ESPERO HABERTE AYUDADO ☺️.\n'
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
            CallbackQueryHandler(pattern='bach_articulo', callback=bach_articulo_callback_handler),
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