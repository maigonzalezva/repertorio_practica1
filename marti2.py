#Grimorios

#Hechizos = Nombre, escuela, poder. rareza, es_prohibido, creador.
hechizos = {
    'H001': ['Llamarada Solar', 'elemental', 5, 'C', False, 'Ignus el Ardiente'],
    'H002': ['Escudo de Escarcha', 'elemental', 3, 'C', False, 'Dama Fenwick'],
    'H003': ['Rayo Astral', 'arcana', 7, 'R', False, 'Magíster Orin'],
    'H004': ['Cadena de Almas', 'oscura', 9, 'L', True, 'El Innombrable'],
    'H005': ['Portal Menor', 'arcana', 4, 'R', False, 'Selene Valdour'],     
    'H006': ['Toque Vampírico', 'oscura', 6, 'R', True, 'Mordath'],
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

def leer_opcion():
    try:
        opcion = int(input("Ingrese su opcion: "))
        if 1<= opcion <= 6:
            return opcion
        else: 
            print("Ingrese un numero entre el 1 y el 6")
            return False
    except ValueError:
        print("Ingrese un numero")
        return False


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
    return None
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
    if buscar_codigo(codigo.upper()):
        reservas.pop(codigo.upper())
        hechizos.pop(codigo.upper())
        return True
    else:
        return False

while True:
    mostrar_menu()
    opcion = leer_opcion()
    if not opcion:
        continue
    if opcion == 1:
        escuela = input("Ingrese el nombre de la escuela (elemental, arcana u oscura): ")
        pergaminos_escuela(escuela)

    elif opcion == 2:
     while True:
         try:
             p_min = int(input("Ingrese el monto minimo ha pagar: "))
             p_max = int(input("Ingrese el monto maximo ha pagar: "))
             if p_min >= 0 and p_min <= p_max:
                busqueda_de_precio(p_min, p_max)
                break
             else:
                     print("El minimo debe ser mayor o igual a 0 y menor que el maximo")
         except ValueError:
                  print("Ingrese un numero entero")

    elif opcion == 3:
        while True:
            codigo = input("Ingrese el codigo del hechizo: ")
            try:
             nuevo_precio = int(input("Ingrese el precio nuevo: "))
            except ValueError:
                print("Ingrese un numero entero")
            
            if actualizar_precio(codigo, nuevo_precio):
                print("Precio actualizado")
            else:
                print("El codigo no existe")

            respuesta = input("¿Desea actualizar otro precio (s/n)?")
            if respuesta == "n":
                break

    elif opcion == 4:
        codigo = input("Ingrese código del hechizo: ")
        nombre = input("Ingrese nombre: ")
        escuela = input("Ingrese escuela: ")
        poder = input("Ingrese poder: ")
        rareza = input("Ingrese rareza: ")
        es_prohibido = input("¿Es prohibido? (s/n): ")
        creador = input("Ingrese creador: ")
        nuevo_precio = input("Ingrese precio: ")
        stock_nuevo = input("Ingrese stock: ")

        if not agregar_hechizo_codigo(codigo):
            print("Codigo invalido o ya existe")
        elif not agregar_hechizo_nombre(nombre):
            print("Nombre invalido")
        elif not agregar_hechizo_nombre_escuela(escuela):
            print("Escuela invalida")
        elif not agregar_hechizo_poder(int(poder)):
            print("Poder invalido")
        elif not agregar_hechizo_rareza(rareza):
            print("Rareza invalida")
        elif agregar_hechizo_es_prohibido(es_prohibido) is None:
            print(("Debe ingresar s o n"))
        elif not agregar_hechizo_creador(creador):
            print("Creador invalido")
        elif not agregar_hechizo_stock(stock_nuevo):
            print("Stock invalido")
        else:
            es_prohibido_bool = agregar_hechizo_es_prohibido(es_prohibido)
            if agregar_hechizo_completo(codigo, nombre, escuela , poder, rareza, es_prohibido,creador, nuevo_precio, stock_nuevo):
             print("Hechizo agregado") 
            else:
             print("El código ya existe")


    elif opcion == 5:
        codigo = input("Ingrese el codigo que desea eliminar: ")
        if eliminar_hechizo(codigo):
            print("Hechizo eliminado")
        else: print("El codigo no existe")
    elif opcion == 6:
        print("El grimorio se cierra. Hasta pronto, aprendiz.")
        break