import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# ### INICIANDO CONEXIÓN CON FIREBASE
# Importando sdk de firebase
cred = credentials.Certificate("firebase_sdk.json")

# Referencia a la BD en tiempo real de FireBase
firebase_admin.initialize_app(cred, {'databaseURL': 'https://epcc-telegram-bot-default-rtdb.firebaseio.com/'})

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
