from telegram import InlineKeyboardMarkup, InlineKeyboardButton
import logging  # Ayuda a ver lo que sucede con el bot y mostrarlo en consola
from botDB import *


# Configuracion de logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s,"
)
logger = logging.getLogger()


#----------------------------------------------------------------
#Botones necesarios para la interaccion secundaria
#----------------------------------------------------------------


#Boton para contacto
btn_contacto = InlineKeyboardButton(
    text='✉️ Contacto de EPCC',
    callback_data="contacto"
)
#Boton para tramites
btn_tramites = InlineKeyboardButton(
    text='🎓 Información de trámites',
    callback_data="tramite"
)
#Boton para terminar la conversación
btn_terminar = InlineKeyboardButton(
    text='Terminar conversación',
    callback_data="terminar"
)
#Botones para bachiler
btn_modo_automatico = InlineKeyboardButton(
    text=' 📃 Modalidad Bachiller Automático - 2021',
    callback_data="bach_automatico"
)
btn_modo_investigacion = InlineKeyboardButton(
    text=' 📃 Modalidad por Trabajo de Investigación',
    callback_data="bach_investigacion"
)
#Botones para titulacion
btn_modo_suficiencia = InlineKeyboardButton(
    text=' 📃 Modalidad Trabajo por suficiencia',
    callback_data="titul_suficiencia"
)
btn_modo_tinvestigacion = InlineKeyboardButton(
    text=' 📃 Modalidad por Trabajo de Investigación',
    callback_data="titul_investigacion"
)
#Boton para regresar a tramite
btn_back_tramite = InlineKeyboardButton(
    text=' ⬅️Atrás',
    callback_data="tramite"
)
# Botones de bachiller
btn_bachiller = InlineKeyboardButton(
    text=' 🎓📃 Trámite para Bachiller',
    callback_data="bachiller"
)
btn_titulacion = InlineKeyboardButton(
    text=' ‍🎓📜‍ Trámite para Titulación',
    callback_data="titulacion"
)



#----------------------------------------------------------------
#Funciones para responder desde la BD a una interaccion de botones
#----------------------------------------------------------------


#Funcion para enviar informacion de secretaria desde un boton
#------------------------------------------------------------
def contacto_callback_handler(update, context):
    user_Name = update.effective_user["first_name"]
    query = update.callback_query   # Recibe el mensaje
    query.answer()  # Requerido. Responde silenciosamente
    logger.info(f'El usuario {user_Name} ha solicitado información de Contacto')

    query.edit_message_text(
        parse_mode='HTML',
        text=' <b>INFORMACIÓN DE CONTACTO DE LA EPCC</b>\n' + string_contacto,
    )


#Funcion para enviar botones de tramites desde un boton
#-----------------------------------------------------------
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

#Funcion para enviar botones de modalidades de bachiller desde un boton
#----------------------------------------------------------------------
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
            [btn_modo_automatico],
            [btn_modo_investigacion],
            [btn_back_tramite]
        ])
    )

#Funcion para enviar informacion de bachiller automatico desde un boton
#----------------------------------------------------------------------
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
        ])
    )
    solicitud_confir(query, update)

#Funcion para enviar informacion de bachiller de investigacion desde un boton
#----------------------------------------------------------------------------
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
        ])
    )
    solicitud_confir(query, update)

#Funcion para enviar botones de modalidades de titulacion desde un boton
#----------------------------------------------------------------------
def titulacion_callback_handler(update, context):
    # Consola retroalimentación
    user_Name = update.effective_user["first_name"]
    logger.info(f'El usuario {user_Name} ha seleccionado Trámites > Titulacion')

    #Actualizando consulta
    query = update.callback_query  # Recibe el mensaje
    query.answer()  # Requerido. Responde silenciosamente


    query.edit_message_text(
        parse_mode='HTML',
        text=f'🤖: Estas son las dos modalidades para obtener el <b>TITULO ACADEMICO</b> 👇',
        reply_markup=InlineKeyboardMarkup([
            [btn_modo_suficiencia],
            [btn_modo_tinvestigacion],
            [btn_back_tramite]
        ])
    )

#Funcion para enviar informacion de titulación por suficiencia desde un boton
#----------------------------------------------------------------------
def titul_suficiencia_callback_handler(update, context):
    # Consola retroalimentación
    user_Name = update.effective_user["first_name"]
    logger.info(f'El usuario {user_Name} ha seleccionado Trámites > Titulacion > Trabajo por Suficiencia')
    
    #Actualizando consulta
    query = update.callback_query  # Recibe el mensaje
    query.answer()  # Requerido. Responde silenciosamente

    query.edit_message_text(
        parse_mode='HTML',
        text='<b>REQUISITOS PARA OBTENER EL TITULO PROFESIONAL</b>\n'
             '<b>MODALIDAD: <em>TRABAJO POR SUFICIENCIA</em></b>\n' + string_titulo_suficiencia,
             reply_markup=InlineKeyboardMarkup([
        ])
    )
    solicitud_confir(query, update)

#Funcion para enviar informacion de titulación por investigacion desde un boton
#----------------------------------------------------------------------
def titul_investigacion_callback_handler(update, context):
    # Consola retroalimentación
    user_Name = update.effective_user["first_name"]
    logger.info(f'El usuario {user_Name} ha seleccionado Trámites > Titulacion > Trabajo de Investigación')
    
    #Actualizando consulta
    query = update.callback_query  # Recibe el mensaje
    query.answer()  # Requerido. Responde silenciosamente

    query.edit_message_text(
        parse_mode='HTML',
        text='<b>REQUISITOS PARA OBTENER EL TITULO PROFESIONAL</b>\n'
             '<b>MODALIDAD: <em>TRABAJO DE INVESTIGACION</em></b>\n' + string_titulo_ti,
             reply_markup=InlineKeyboardMarkup([
        ])
    )
    solicitud_confir(query, update)

def terminar_callback_handler(update, context):
    user_Name = update.effective_user["first_name"]
    query = update.callback_query   # Recibe el mensaje
    query.answer()  # Requerido. Responde silenciosamente

    query.edit_message_text(
        parse_mode='HTML',
        text=f' <b>🤖: Aqui tienes lo solicitado ☺️.</b>\n'
             f'🤖: Si hay algo mas en lo que pueda ayudarte, escríbeme...',
    )

#Funcion que confirma la entrega de lo solicitado
#-----------------------------------------------
def solicitud_confir(update, context):
  bot = context.bot
  chatId = update.message.chat_id

  bot.sendMessage(#se enviara un mensaje al chat
    chat_id = chatId,
    text = f'🤖: ¡Bien!, la informacion que solicitaste es esta 👆🏻:\n'
           f'🤖: ¿Algo más que necesites 😊?'
  )