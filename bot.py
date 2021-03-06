# BOT TELEGRAM : CONSULTAS EPCC
#-------------------------------
# Implementaci贸n de di谩logo


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
    logger.info(f'El usuario {user_Name} ha solicitado informaci贸n(/infoBot) sobre el bot')

    bot.sendMessage(
        chat_id=chat_Id,
        parse_mode="HTML",
        text=f'Hola soy el bot 馃 de la <b>Escuela Profesional de Ciencia de la Computaci贸n - UNSA</b>.'
             f'Si necesitas informaci贸n sobre tr谩mites de Bachiller y T铆tulo Profesional '
             f'puedo ayudarte. Comienza escribiendo /start. \n' 
             f'Tambi茅n puedes escribirme en el chat y tratar茅 de mostrarte la informaci贸n m谩s adecuada.'  # 2da manera de responder
    )

# # Botones
btn_contacto = InlineKeyboardButton(
    text='鉁夛笍 Contacto de EPCC',
    callback_data="contacto"
)
btn_tramites = InlineKeyboardButton(
    text='馃帗 Informaci贸n de tr谩mites',
    callback_data="tramite"
)
btn_terminar = InlineKeyboardButton(
    text='Terminar conversaci贸n',
    callback_data="terminar"
)

# Botones
btn_modo_articulo = InlineKeyboardButton(
        text=' 馃搩 Modalidad por Art铆culo de Publicaci贸n',
        callback_data="bach_articulo"
    )
btn_modo_proyecto = InlineKeyboardButton(
        text=' 馃搩 Modalidad por Trabajo de Investigaci贸n',
        callback_data="bach_investigacion"
    )
btn_back = InlineKeyboardButton(
        text=' 猬咃笍Atr谩s',
        callback_data="tramite"
    )

def start(update, context):
    bot = context.bot
    # chat_Id = update.message.chat_id
    user_Name = update.effective_user["first_name"]
    logger.info(f'El usuario {user_Name} ha iniciado(/start) el bot')   # Consola retroalimentaci贸n

    # Lo que se muestra al ejecutar el comando /start
    update.message.reply_text(
        text=f'Hola {user_Name} 鈽猴笍.Gracias por usar nuestro bot.\n'
             f'馃: A continuaci贸n te mostrar茅 los tipos de informaci贸n que puedo brindarte. '
             f'S贸lo toca la opci贸n que te interesa:',
        reply_markup=InlineKeyboardMarkup([
            [btn_contacto],
            [btn_tramites]
        ])
    )

# Mensaje maneja la conversaci贸n con el bot
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
                text='馃: 隆Perfecto!\n'
                     '馃: Elige una de las opciones:',
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
            text=f'馃: Estas son las dos modalidades para obtener el <b>Grado de Bachiller</b> 馃憞',
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
                text='馃: 隆Perfecto!\n'
                     '馃: Elige una de las opciones:',
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
            text=f'馃: Estas son las dos modalidades para obtener el <b>Grado de Bachiller</b> 馃憞',
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
    logger.info(f'El usuario {user_Name} ha solicitado informaci贸n de Contacto')

    query.edit_message_text(
        parse_mode='HTML',
        text=' <b>INFORMACI脫N DE CONTACTO DE LA EPCC</b>\n'
             '鈻笍Correo electr贸nico: epcc@unsa.edu.pe\n'
             '鈻笍Tel茅fono: 949107364 (Secretar铆a Raquel)\n'
             '鈻笍Horario de atenci贸n: Lunes a viernes de 8:30 a 10:30AM (v铆a Meet) \n'
             '鈻? Meet de atenci贸n: meet.google.com/smh-igaw-vze\n'
    )
    bot_feedback(query, update)

## bot feedback
def bot_feedback(update, context):
    # update.message.reply_photo(
    #     'https://drive.google.com/file/d/1aXFhaBXeS3DpxB10KmJx13m645V4mWrl/view?usp=sharing')
    # update.message.reply_text(  # se enviara un mensaje al chat
    #     parse_mode='HTML',
    #     text=' <b>INFORMACI脫N DE CONTACTO DE LA EPCC</b>\n'
    #          '鈻笍Correo electr贸nico: epcc@unsa.edu.pe\n'
    #          '鈻笍Tel茅fono: 949107364 (Secretar铆a Raquel)\n'
    #          '鈻笍Horario de atenci贸n: Lunes a viernes de 8:30 a 10:30AM (v铆a Meet) \n'
    #          '鈻? Meet de atenci贸n: meet.google.com/smh-igaw-vze\n'
    # )
    update.message.reply_text(  # se enviara un mensaje al chat
        text=f'馃: Aqu铆 tienes lo solicitado 鈽猴笍.\n'
             f'馃: Si hay algo mas en lo que pueda ayudarte, escr铆beme...\n'
    )

## botones de tramites

btn_bachiller = InlineKeyboardButton(
    text=' 馃帗馃搩 Tr谩mite para Bachiller',
    callback_data="bachiller"
)
btn_titulacion = InlineKeyboardButton(
    text=' 鈥嶐煄擆煋溾?? Tr谩mite para Titulaci贸n',
    callback_data="titulacion"
)


def tramites_callback_handler(update, context):
    # Consola retroalimentaci贸n
    user_Name = update.effective_user["first_name"]
    logger.info(f'El usuario {user_Name} ha seleccionado Tr谩mites')

    #Actualizando consulta
    query = update.callback_query  # Recibe el mensaje
    query.answer()  # Requerido. Responde silenciosamente

    query.edit_message_text(
        parse_mode='HTML',
        text=f'馃: {user_Name}, estos son los tr谩mites de los que puedo brindarte informaci贸n 馃檪 ',
        reply_markup=InlineKeyboardMarkup([
            [btn_bachiller],
            [btn_titulacion]
        ])
    )

def titulacion_callback_handler(update, context):
    # Consola retroalimentaci贸n
    user_Name = update.effective_user["first_name"]
    logger.info(f'El usuario {user_Name} ha seleccionado Tr谩mites > Titulacion')
    # boton
    btn_back = InlineKeyboardButton(
        text=' 猬咃笍Atr谩s',
        callback_data="tramite"
    )
    #Actualizando consulta
    query = update.callback_query  # Recibe el mensaje
    query.answer()  # Requerido. Responde silenciosamente

    query.edit_message_text(
        parse_mode='HTML',
        text='<b>REQUISITOS PARA OBTENER EL TITULO PROFESIONAL</b>\n'
             '鈻笍Solicitud dirigida al Decano de la facultad en formato UNSA.\n'
             '鈻笍Recibo de pago de expedito para optar el T铆tulo Profesional.\n'
             '鈻笍Trabajo de investigaci贸n digitalizado en formato PDF. \n'
             '鈻笍Constancia emitida por la Biblioteca Virtual de autorizaci贸n de publicaci贸n en el portal de Tesis '
             'Electr贸nicas. \n'
             '鈻笍Certificado negativo de antecedentes penales.\n'
             '鈻笍Certificado oficial de estudios.\n'
             '鈻笍Copia legalizada de DNI en formato A5. \n'
             '鈻笍Copia legalizada del Grado de Bachiller. \n'
             '鈻笍Fotograf铆a tama帽o pasaporte a color fondo blanco. \n'
             '鈻笍Constancia de Egresado. \n'
             '鈻笍Constancia que acredite dominio de nivel intermedio de idioma extranjero.\n'
             '鈻笍Constacia de inscripci贸n a SUNEDU del Grado Acad茅mico de Bachiller. \n'
             '鈻笍Constancia de no adeudar Bienes. \n'
             '鈻笍Constancia de Biblioteca. \n'
             '鈻笍Recibo de Subdirecci贸n de Finanzas de pago de los derechos por todos los conceptos.\n',
        reply_markup=InlineKeyboardMarkup([
            [btn_back]
        ])
    )
    terminar(query, update)



def bachiller_callback_handler(update, context):
    # Consola retroalimentaci贸n
    user_Name = update.effective_user["first_name"]
    logger.info(f'El usuario {user_Name} ha seleccionado Tr谩mites > Bachiller')

    #Actualizando consulta
    query = update.callback_query  # Recibe el mensaje
    query.answer()  # Requerido. Responde silenciosamente

    

    query.edit_message_text(
        parse_mode='HTML',
        text=f'馃: Estas son las dos modalidades para obtener el <b>Grado de Bachiller</b> 馃憞',
        reply_markup=InlineKeyboardMarkup([
            [btn_modo_articulo],
            [btn_modo_proyecto],
            [btn_back]
        ])
    )


def bach_articulo_callback_handler(update, context):
    # Consola retroalimentaci贸n
    user_Name = update.effective_user["first_name"]
    logger.info(f'El usuario {user_Name} ha seleccionado Tr谩mites > Bachiller > Art铆culo Cient铆fico')
    btn_back = InlineKeyboardButton(
        text=' 猬咃笍Atr谩s',
        callback_data="bachiller"
    )
    # Actualizando consulta
    query = update.callback_query  # Recibe el mensaje
    query.answer()  # Requerido. Responde silenciosamente

    query.edit_message_text(
        parse_mode='HTML',
        text='<b>REQUISITOS PARA OBTENER EL GRADO ACAD脡MICO DE BACHILLER</b>\n'
             '<b>MODALIDAD: <em>ART脥CULO DE PUBLICACI脫N</em></b>\n'
             '鈻笍Pronto m谩s informaci贸n de esta modalidad.\n',
        reply_markup=InlineKeyboardMarkup([
            [btn_back]
        ])
    )


def bach_investigacion_callback_handler(update, context):
    # Consola retroalimentaci贸n
    user_Name = update.effective_user["first_name"]
    logger.info(f'El usuario {user_Name} ha seleccionado Tr谩mites > Bachiller > Trabajo de Invetigaci贸n')
    # button
    btn_back = InlineKeyboardButton(
        text=' 猬咃笍Atr谩s',
        callback_data="bachiller"
    )
    # Actualizando consulta
    query = update.callback_query  # Recibe el mensaje
    query.answer()  # Requerido. Responde silenciosamente

    query.edit_message_text(
        parse_mode='HTML',
        text='<b>REQUISITOS PARA OBTENER EL GRADO ACAD脡MICO DE BACHILLER</b>\n'
             '<b>MODALIDAD: <em>TRABAJO DE INVESTIGACI脫N</em></b>\n'
             '鈻笍Solicitud dirigida al Decano de la facultad en formato UNSA.\n'
             '鈻笍Trabajo de investigaci贸n digitalizado en formato PDF. \n'
             '鈻笍Constancia emitida por la Biblioteca Virtual de autorizaci贸n de publicaci贸n en el Repositorio.\n'
             '鈻笍Certificado negativo de antecedentes penales.\n'
             '鈻笍Certificado oficial de estudios.\n'
             '鈻笍Copia legalizada de DNI en formato A5. \n'
             '鈻笍Fotograf铆a tama帽o pasaporte a color fondo blanco. \n'
             '鈻笍Constancia de Egresado. \n'
             '鈻笍Constancia que acredite dominio de nivel intermedio de idioma extranjero.\n'
             '鈻笍Constancia de no adeudar Bienes a la facultad. \n'
             '鈻笍Constancia de no adeudar material bibliogr谩fico (Direcci贸n general de Biblioteca). \n'
             '鈻笍Recibo de Subdirecci贸n de Finanzas de pago de los derechos por todos los conceptos. \n',
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
        text=f'馃: ESPERO HABERTE AYUDADO 鈽猴笍.\n'
    )


# Funciones auxiliares para la conversaci贸n

def terminar(update, update1):
    userName = update1.effective_user['first_name']
    update.message.reply_text(  # se enviara un mensaje al chat
        parse_mode='HTML',
        text=f'馃: ESPERO HABERTE AYUDADO 鈽猴笍.\n'
    )

# Main Function
if __name__ == '__main__':
    mybot = telegram.Bot(token=TOKEN)
    print(mybot.getMe())  # Muestra en consola informaci贸n sobre el bot

    # Updater: se conecta y recibe los mensajes
    updater = Updater(mybot.token, use_context=True)

    # Crear el 'despachador'
    dp = updater.dispatcher

    # Crear comando y el m茅todo (acci贸n del comando)
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("info", getBotInfo))
    dp.add_handler(MessageHandler(Filters.text, mensaje))   # Maneja las key words para la conversaci贸n

    # Crear el callback handler
    # ConversationHandler define como ser谩 la conversaci贸n
    dp.add_handler(ConversationHandler(
        entry_points=[
            # Al recibir el patron definido en el data del bot贸n ejecuta la funcion callback
            CallbackQueryHandler(pattern='contacto', callback=contacto_callback_handler),
            CallbackQueryHandler(pattern='tramite', callback=tramites_callback_handler),
            CallbackQueryHandler(pattern='bachiller', callback=bachiller_callback_handler),
            CallbackQueryHandler(pattern='titulacion', callback=titulacion_callback_handler),
            CallbackQueryHandler(pattern='bach_articulo', callback=bach_articulo_callback_handler),
            CallbackQueryHandler(pattern='bach_investigacion', callback=bach_investigacion_callback_handler),
            CallbackQueryHandler(pattern='terminar', callback=terminar_callback_handler) #Terminar conversaci贸n
        ],
        states={},
        fallbacks=[]
    ))

    # Preguntar por mensajes entrantes to do el tiempo
    updater.start_polling()

    # Terminar bot con ctrl + c
    updater.idle()