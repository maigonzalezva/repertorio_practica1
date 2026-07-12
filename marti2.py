#Grimorios

#Hechizos = Nombre, escuela, poder. rareza, es_prohibido, creador.
hechizos = {
    'H001': ['Llamarada Solar', 'elemental', 5, 'C', False, 'Ignus el Ardiente'],
    'H002': ['Escudo de Escarcha', 'elemental', 3, 'C', False, 'Dama Fenwick'],
    'H003': ['Rayo Astral', 'arcana', 7, 'R', False, 'Magíster Orin'],
    'H004': ['Cadena de Almas', 'oscura', 9, 'L', True, 'El Innombrable'],
    'H005': ['Portal Menor', 'arcana', 4, 'R', False, 'Selene Valdour'],     'H006': ['Toque Vampírico', 'oscura', 6, 'R', True, 'Mordath'],
}

#Reservas= Precio, stock
reservas = {     
    'H001': [120, 8],     
    'H002': [90, 0],
    'H003': [340, 3],
    'H004': [999, 2],
    'H005': [210, 5],
    'H006': [450, 4],

}

def mostrar_menu():
    print('''========= GRIMORIO ASTRALIS =========
            1.	Pergaminos por escuela de magia
            2.	Búsqueda de hechizos por rango de precio
            3.	Actualizar precio de hechizo
            4.	Agregar hechizo
            5.	Eliminar hechizo
            6.	Salir
            =====================================
            ''')

def pergaminos_escuela(escuela):
   total_pergaminos = 0
   for codigo, datos in hechizos.items():
       if datos[1] == escuela.lower():
           total_pergaminos += reservas[codigo][1]
   print(f"El total de pergaminos disponibles es: {total_pergaminos}")


def busqueda_de_precio(p_min, p_max):
    resultado = []
    for codigo, datos in reservas.items():
        if datos[0] >= p_min and datos[0] <= p_max and datos[1] != 0:
                resultado.append(f"{hechizos[codigo][0]}--{codigo}")
    resultado.sort()
    
    if len(resultado) == 0:
        print("No hay hechizos en ese rango de precios")
    else:
        print(f"Los hechizos encontrados son: {resultado}")


def buscar_codigo(codigo):
    if codigo.upper() in reservas:
        return True
    return False
        
def actualizar_precio(codigo, nuevo_precio):
    if buscar_codigo(codigo.upper()):
        reservas[codigo.upper()][0] = nuevo_precio
        return True
    else:
        return False
    
def agregar_hechizo_codigo(codigo):
    if codigo.strip() == "":
        return False
    if (buscar_codigo(codigo)):
        return False
    
    return True

def agregar_hechizo_nombre(nombre):
    if nombre.strip() == "":
        return False
    else: 
        return True
    
def agregar_hechizo_nombre_escuela(escuela):
    escuela = escuela.lower()
    if escuela == "elemental" or escuela == "arcana" or escuela == "oscura":
        return True
    else:
        return False

def agregar_hechizo_poder(poder):
    if poder > 0:
        return True
    else:
        return False

def agregar_hechizo_rareza(rareza):
    if rareza.upper() in ["C", "R", "L"]:
        return True
    else:
        return False

def agregar_hechizo_es_prohibido(es_prohibido):
    if es_prohibido == "s":
        return True
    else:
        if es_prohibido == "n":
         return False

def agregar_hechizo_creador(creador):
    if creador.strip() == "":
        return False
    return True

def agregar_hechizo_precio(precio_nuevo):
    try:
        if int(precio_nuevo) > 0:
            return True
        else:
            return False

    except ValueError:
        return False

def agregar_hechizo_stock(stock_nuevo):
    try:
        if int(stock_nuevo) >= 0: 
            return True
        else: 
            return False
    except ValueError:
        return False


def agregar_hechizo_completo(codigo, nombre, escuela , poder, rareza, es_prohibido,creador, precio_nuevo, stock_nuevo):
    if buscar_codigo(codigo):
        return False

    hechizos[codigo] = [nombre, escuela, int(poder), rareza, es_prohibido, creador]
    reservas[codigo] = [int(precio_nuevo), int(stock_nuevo)]
    return True

def eliminar_hechizo(codigo):
    if buscar_codigo == True:
        reservas.pop(codigo)
        hechizos.pop(codigo)
        return True
    else:
        return False
