from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from Bnts import *


#Funcion que verifica las pálabras recibidas
#-------------------------------------------
def verificar(lista):
    
    hello = [['ho','Ho','la','ol'],['Bu','bu','en','nas','nos']]
    pal = ['ba','Ba','chi','lle']
    pal2 = ['Ti','ti','tí','Tí','tul','lo','lac']
    pal_1 = ['Inv','inv','vest','est','tig','gac']
    pal_2 = ['Suf','suf','fic','cien','nci','cia']
    pal_3 = ['Aut','aut','uto','toma','mati','tico']
    pal3 = [['Se','se','cre','ta'],['Es','es','scu','ela','la'],['Con','con','nta','act']]
    consul = ['Con','con','ons','nsu','sul','ult','lta']
    fin = ['gra','Gra','cia','ci','as']
    cont = 0
    r_hello = False
    r_pal = False
    r_pal_1 = False
    r_pal_2 = False
    r_pal_3 = False
    r_pal2 = False
    r_pal3 = False
    r_consul = False
    r_fin = False
    
    for i in range(len(lista)):
        for h in range(len(hello)):
            for n in range(len(hello[h])):
                if hello[h][n] in lista[i]:
                    cont = cont+1
                if cont >=3:
                    cont = 0
                    r_hello = True
                    break
            if r_hello:
                break

    for i in range(len(lista)):
        for j in range(len(pal)):
            if pal[j] in lista[i]:
                cont = cont+1
            if cont >=3:
                cont = 0
                r_pal = True
                break
    
    for i in range(len(lista)):
        for k in range(len(pal2)):
            if pal2[k] in lista[i]:
                cont = cont+1
            if cont >=3:
                cont = 0
                r_pal2 = True
                break
    
    for i in range(len(lista)):
        for l in range(len(pal3)):
            for m in range(len(pal3[l])):
                if pal3[l][m] in lista[i]:
                    cont = cont+1
                if cont >=3:
                    cont = 0
                    r_pal3 = True
                    break
            if r_pal3:
                break
    
    for i in range(len(lista)):
        for k in range(len(fin)):
            if fin[k] in lista[i]:
                cont = cont+1
            if cont >=3:
                cont = 0
                r_fin = True
                break

    for i in range(len(lista)):
        for j in range(len(consul)):
            if consul[j] in lista[i]:
                cont = cont+1
            if cont >=3:
                cont = 0
                r_consul = True
                break

    for i in range(len(lista)):
        for j in range(len(pal_1)):
            if pal_1[j] in lista[i]:
                cont = cont+1
            if cont >=3:
                cont = 0
                r_pal_1 = True
                break

    for i in range(len(lista)):
        for j in range(len(pal_2)):
            if pal_2[j] in lista[i]:
                cont = cont+1
            if cont >=3:
                cont = 0
                r_pal_2 = True
                break

    for i in range(len(lista)):
        for j in range(len(pal_3)):
            if pal_3[j] in lista[i]:
                cont = cont+1
            if cont >=3:
                cont = 0
                r_pal_3 = True
                break

 #Condicionales para saber si hay mezclaz de palabras
 #-----------------------------------------------
    if r_hello:
        if r_pal:
            if r_pal2:
                return 2
            if r_pal_1:
                return 12 
            if r_pal_3:
                return 13
            return 3
        if r_pal2:
            if r_pal_1:
                return 14
            if r_pal_2:
                return 15
            return 4
        if r_pal3:
            return 5
        return 1
  
    if r_pal:
        if r_pal2:
            return 6
        return 7
    
    if r_pal:
        if r_pal_1:
            return 16 
        if r_pal_3:
            return 17

    if r_pal2:
        if r_pal_1:
            return 18 
        if r_pal_2:
            return 19

    if r_pal2:
        return 8

    if r_pal3:
        return 9
  
    if r_fin:
        return 10
  
    if r_consul:
        return 11
 
#Funcion cuando se recibe solo un "hola"
#-------------------------------------------
def hola(update, context):
    bot = context.bot
    chatId = update.message.chat_id
    userName = update.effective_user['first_name']

    bot.sendMessage(  # se enviara un mensaje al chat
        chat_id=chatId,
        text=f'🤖: ¡Hola {userName}! ☺️, gracias por invocarme, espero que estes muy bien. '
            f' ¿En qué puedo ayudarte?'
    )

#Funcion cuando se recibe un "hola" y una pal
#-------------------------------------------
def hola_uni(update, context):
    bot = context.bot
    chatId = update.message.chat_id
    userName = update.effective_user['first_name']

    bot.sendMessage(  # se enviara un mensaje al chat
        chat_id=chatId,
        text=f'🤖: ¡Hola {userName}! ☺️, espero que estes muy bien. '
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


#----------------------------------------------------------------
#Funciones para responder desde la BD a una interaccion de puro mensajes
#----------------------------------------------------------------


#Funcion para enviar infromacion de secretaria
#--------------------------------------------------
def contac(update,context):
    bot = context.bot
    chatId = update.message.chat_id
    userName = update.effective_user['first_name']

    bot.sendMessage(  # se enviara un mensaje al chat
        chat_id = chatId,
        parse_mode='HTML',
        text=' <b>INFORMACIÓN DE CONTACTO DE LA EPCC</b>\n' + string_contacto,

    )

#Funcion que entrega el bachiller
#-----------------------------------------------
def tramites(update, context):
    user_Name = update.effective_user["first_name"]
    bot = context.bot
    chatId = update.message.chat_id
    bot.sendMessage(
            chat_id=chatId,
            parse_mode='HTML',
            text='🤖: ¡Perfecto!\n'
                 '🤖: Elige una de las opciones:',
            reply_markup=InlineKeyboardMarkup([
                [btn_bachiller],
                [btn_titulacion],
                [btn_terminar]
                ])
            )

#Funcion que entrega el bachiller
#-----------------------------------------------
def bachiller(update, context):
    bot = context.bot
    chatId = update.message.chat_id
    bot.sendMessage(
            chat_id=chatId,
            parse_mode='HTML',
            text=f'🤖: Estas son las dos modalidades para obtener el <b>Grado de Bachiller</b> 👇',
            reply_markup=InlineKeyboardMarkup([
                [btn_modo_automatico],
                [btn_modo_investigacion],
                ])
            )


#Funcion que entrega el bachiller por investigacion
#-----------------------------------------------
def bachiller_investigacion(update, context):
    bot = context.bot
    chatId = update.message.chat_id

    bot.sendMessage(#se enviara un mensaje al chat
        chat_id = chatId,
        parse_mode='HTML',
        text='<b>REQUISITOS PARA OBTENER EL GRADO ACADÉMICO DE BACHILLER</b>\n'
            '<b>MODALIDAD: <em>TRABAJO DE INVESTIGACIÓN</em></b>\n' + string_bach_ti,
        )


#Funcion que entrega el bachiller automatico
#-----------------------------------------------
def bachiller_automatico(update, context):
    bot = context.bot
    chatId = update.message.chat_id

    bot.sendMessage(#se enviara un mensaje al chat
        chat_id = chatId,
        parse_mode='HTML',
        text='<b>REQUISITOS PARA OBTENER EL GRADO ACADÉMICO DE BACHILLER</b>\n' 
            '<b>MODALIDAD: <em>BACHILLER AUTOMÁTICO 2021</em></b>\n' + string_bach_automatico,
        )

#Funcion que entrega el bachiller
#-----------------------------------------------
def titulo(update, context):
    bot = context.bot
    chatId = update.message.chat_id
    bot.sendMessage(
            chat_id=chatId,
            parse_mode='HTML',
            text=f'🤖: Estas son las dos modalidades para obtener el <b>Grado de Bachiller</b> 👇',
            reply_markup=InlineKeyboardMarkup([
                [btn_modo_suficiencia],
                [btn_modo_tinvestigacion],
                ])
            )



#Funcion que entrega el titulo investigacion
#-----------------------------------------------
def titulo_investigacion(update, context):
    bot = context.bot
    chatId = update.message.chat_id

    bot.sendMessage(#se enviara un mensaje al chat
        chat_id = chatId,
        parse_mode='HTML',
        text='<b>REQUISITOS PARA OBTENER EL TITULO PROFESIONAL</b>\n'
            '<b>MODALIDAD: <em>TRABAJO DE INVESTIGACIÓN</em></b>\n' + string_titulo_ti,
        )

#Funcion que entrega el titulo suficiencia
#-----------------------------------------------
def titulo_suficiencia(update, context):
    bot = context.bot
    chatId = update.message.chat_id

    bot.sendMessage(#se enviara un mensaje al chat
        chat_id = chatId,
        parse_mode='HTML',
        text='<b>REQUISITOS PARA OBTENER EL TITULO PROFESIONAL</b>\n'
            '<b>MODALIDAD: <em>TRABAJO POR SUFICIENCIA</em></b>\n' + string_titulo_suficiencia,
                )

#Funcion que termina la converación
#-----------------------------------------------
def fin(update, context):
    bot = context.bot
    chatId = update.message.chat_id
    userName = update.effective_user['first_name']

    bot.sendMessage(  # se enviara un mensaje al chat
        chat_id = chatId,
        text=f'🤖: Gracias por escribirme {userName}.\n'
            f'🤖: Si hay algo mas en lo que pueda ayudarte, Escribeme...\n'
            f'🤖: Hasta ello cuidate mucho',
    )

#Funcion que pide información mas especifica
#-----------------------------------------------
def consultas_noespecifico(update, context):
    bot = context.bot
    chatId = update.message.chat_id
    userName = update.effective_user['first_name']

    bot.sendMessage(  # se enviara un mensaje al chat
        chat_id = chatId,
        text=f'🤖: {userName} 😊,\n'
            f'🤖: ¿Que información necesitas especificamente?\n',
    )
  