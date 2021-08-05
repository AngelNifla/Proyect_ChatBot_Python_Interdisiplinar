def verificar(lista):

# Key words
# badWord = ['hol', 'Hol', 'Buenos', 'buenos', 'Buenas', 'buenas']
# badWord1 = ['consultar', 'Consultar', 'Buscando', 'buscando', 'Información', 'información', 'informacion',
#           'Informacion']
# badWord2 = ['Título', 'título', 'Titulo', 'titulo', 'Bachiller', 'bachiller', 'Tramitar', 'tramitar', 'Tramites',
#           'tramites', 'trámites', 'Trámites']
# badWord3 = ['Secretaría', 'secretaría', 'Contacto', 'contacto', 'escuela']

hello = [['ho', 'Ho', 'la', 'ol', ], ['Bu', 'bu', 'en', 'nas', 'nos']]
pal = ['ba', 'Ba', 'chi', 'lle']
pal2 = ['Ti', 'ti', 'tí', 'Tí', 'tul', 'lo', 'lac']
pal3 = [['Se', 'se', 'cre', 'ta'], ['Es', 'es', 'scu', 'ela', 'la'], ['Con', 'con', 'nta', 'act']]
consul = ['Con', 'con', 'ons', 'nsu', 'sul', 'ult', 'lta']
fin = ['gra', 'Gra', 'cia', 'ci', 'as']
cont = 0
r_hello = False
r_pal = False
r_pal2 = False
r_pal3 = False
r_consul = False
r_fin = False

for i in range(len(lista)):
    for h in range(len(hello)):
        for n in range(len(hello[h])):
            if hello[h][n] in lista[i]:
                cont = cont + 1
            if cont >= 3:
                cont = 0
                r_hello = True
                break
        if r_hello:
            break

for i in range(len(lista)):
    for j in range(len(pal)):
        if pal[j] in lista[i]:
            cont = cont + 1
        if cont >= 3:
            cont = 0
            r_pal = True
            break

for i in range(len(lista)):
    for k in range(len(pal2)):
        if pal2[k] in lista[i]:
            cont = cont + 1
        if cont >= 3:
            cont = 0
            r_pal2 = True
            break

for i in range(len(lista)):
    for l in range(len(pal3)):
        for m in range(len(pal3[l])):
            if pal3[l][m] in lista[i]:
                cont = cont + 1
            if cont >= 3:
                cont = 0
                r_pal3 = True
                break
        if r_pal3:
            break

for i in range(len(lista)):
    for k in range(len(fin)):
        if fin[k] in lista[i]:
            cont = cont + 1
        if cont >= 3:
            cont = 0
            r_fin = True
            break

for i in range(len(lista)):
    for j in range(len(consul)):
        if consul[j] in lista[i]:
            cont = cont + 1
        if cont >= 3:
            cont = 0
            r_consul = True
            break

if r_hello:
    if r_pal:
        if r_pal2:
            return 2
        return 3
    if r_pal2:
        return 4
    if r_pal3:
        return 5
    return 1

if r_pal:
    if r_pal2:
        return 6
    return 7

if r_pal2:
    return 8

if r_pal3:
    return 9

if r_fin:
    return 10

if r_consul:
    return 11


def hola(update, context):
    bot = context.bot
    chatId = update.message.chat_id
    userName = update.effective_user['first_name']

    bot.sendMessage(  # se enviara un mensaje al chat
        chat_id=chatId,
        text=f'🤖: ¡Hola {userName}! ☺️, gracias por invocarme, espero que estes muy bien. '
             f' ¿En qué puedo ayudarte?'
    )


def hola_uni(update, context):
    bot = context.bot
    chatId = update.message.chat_id
    userName = update.effective_user['first_name']

    bot.sendMessage(  # se enviara un mensaje al chat
        chat_id=chatId,
        text=f'🤖: ¡Hola {userName}! ☺️, espero que estes muy bien. '
    )


def bachi(update, context):
    bot = context.bot
    chatId = update.message.chat_id

    bot.sendMessage(  # se enviara un mensaje al chat
        chat_id=chatId,
        text=f'🤖: ¡Bien!, la informacion que solicitaste es esta:\n'
    )


def titul(update, context):
    bot = context.bot
    chatId = update.message.chat_id

    bot.sendMessage(  # se enviara un mensaje al chat
        chat_id=chatId,
        text=f'🤖: ¡Bien!, esto es lo que se necesita:\n'
    )
    bot.sendMessage(  # se enviara un mensaje al chat
        chat_id=chatId,
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


def contac(update, context):
    bot = context.bot
    chatId = update.message.chat_id
    userName = update.effective_user['first_name']

    bot.sendMessage(  # se enviara un mensaje al chat
        chat_id=chatId,
        text=f'🤖: 👇 Esto es lo que solicitaste {userName}.\n'

    )

    bot.sendMessage(  # se enviara un mensaje al chat
        chat_id=chatId,
        parse_mode='HTML',
        text=' <b>INFORMACIÓN DE CONTACTO DE LA EPCC</b>\n'
             '▫️Correo electrónico: epcc@unsa.edu.pe\n'
             '▫️Teléfono: 949107364 (Secretaría Raquel)\n'
             '▫️Horario de atención: Lunes a viernes de 8:30 a 10:30AM (vía Meet) \n'
             '▫ Meet de atención: meet.google.com/smh-igaw-vze\n'
    )


def fin(update, context):
    bot = context.bot
    chatId = update.message.chat_id
    userName = update.effective_user['first_name']

    bot.sendMessage(  # se enviara un mensaje al chat
        chat_id=chatId,
        text=f'🤖: Gracias por escribirme {userName}.\n'
             f'🤖: Si hay algo mas en lo que pueda ayudarte, Escribeme...\n'
             f'🤖: Hasta ello cuidate mucho',
    )


def consultas_noespecifico(update, context):
    bot = context.bot
    chatId = update.message.chat_id
    userName = update.effective_user['first_name']

    bot.sendMessage(  # se enviara un mensaje al chat
        chat_id=chatId,
        text=f'🤖: {userName} 😊,\n'
             f'🤖: ¿Que información necesitas especificamente?\n',
    )
