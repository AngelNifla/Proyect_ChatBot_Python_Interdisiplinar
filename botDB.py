import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# ### INICIANDO CONEXIÓN CON FIREBASE
# Importando sdk de firebase
cred = credentials.Certificate("E:\PYTHON DATE\Prueva_47\Firebase_sdk.json")

# Referencia a la BD en tiempo real de FireBase
firebase_admin.initialize_app(cred, {'databaseURL': 'https://bot-python-telegram-basedatos-default-rtdb.firebaseio.com/'})

# ### LECTURA DE BASE DE INFORMACIÓN EN BASE DE DATOS ###
# Referencia a estructura de DataBase
ref_DB = db.reference('/')
bot_DB = ref_DB.get()  # return dict type

list_child_DB = list(bot_DB)  # Hijos de root
main_nodo = list_child_DB[0]  # key del 1er nodo donde se almacena la informacion a mostrar en el bot


# ### Funciones
def select_list_info(tramite):
    """ Devuelve la lista de:
        0: contacto,
        1: bachiller automatico,
        2: bachiller trabajo investigacion,
        3: titulo trabajo investigacion,
        4: titulo suficiencia"""
    if tramite == 0:
        ref_contacto = db.reference(main_nodo + '/Contacto')
        print("Creando lista de info Contacto")
        return ref_contacto.get()  # return a list type
    elif tramite == 1:
        ref_bach_auto = db.reference(main_nodo + '/Bachiller-Automatico')
        print("Creando lista de info Bachiller Automático")
        return ref_bach_auto.get()  # return a list type
    elif tramite == 2:
        ref_bach_ti = db.reference(main_nodo + '/Bachiller-TI')
        print("Creando lista de info Bachiller Trabajo investigacion")
        return ref_bach_ti.get()  # return a list type
    elif tramite == 3:
        ref_titulo_ti = db.reference(main_nodo + '/Titulo-TI')
        print("Creando lista de info Titulo Trabajo de investigación")
        return ref_titulo_ti.get()  # return a list type
    elif tramite == 4:
        ref_titulo_suf = db.reference(main_nodo + '/Titulo-suficiencia')
        print("Creando lista de info Titulo suficiencia")
        return ref_titulo_suf.get()  # return a list type


def print_requisitos(list_requerimientos, col_name, id_show=True):
    """Pasar una lista con los requesitos, la clave de acceso a columna, si se muestra id,"""
    for row_req in list_requerimientos:
        if isinstance(row_req, dict) and id_show is True:
            print(str(row_req['Id']) + '. ' + row_req[col_name])
        elif isinstance(row_req, dict) and id is False:
            print(row_req[col_name])


# print('REQUISITOS BACHILLER \n')
# print_requisitos(select_list_info(0), 'Información', True)


# Obtener informacion de BD y construcción de string
#---------------------------------------------------------
list_info_contacto = select_list_info(0)
string_contacto =''
for row in list_info_contacto:
    if isinstance(row, dict):
        string_contacto += '▫️<b>' + row['Tipo Informacion'] + ':</b> ' + row['Información'] + '\n'

req_bach_automatico = select_list_info(1)
string_bach_automatico =''
for row in req_bach_automatico:
    if isinstance(row, dict):
        string_bach_automatico += '▫️<b>' + str(row['Id']) + '.</b> ' + row['Requisito'] + '\n'

req_bach_ti = select_list_info(2)
string_bach_ti =''
for row in req_bach_ti:
    if isinstance(row, dict):
        string_bach_ti += '▫️<b>' + str(row['Id']) + '.</b> ' + row['Requisito'] + '\n'

req_titulo_ti = select_list_info(3)
string_titulo_ti =''
for row in req_titulo_ti:
    if isinstance(row, dict):
        string_titulo_ti += '▫️<b>' + str(row['Id']) + '.</b> ' + row['Requisito'] + '\n'

req_titulo_suficiencia = select_list_info(4)
string_titulo_suficiencia =''
for row in req_titulo_suficiencia:
    if isinstance(row, dict):
        string_titulo_suficiencia += '▫️<b>' + str(row['Id']) + '.</b> ' + row['Requisito'] + '\n'
