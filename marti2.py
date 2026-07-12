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
    try:
     opcion = int(input("Ingrese una opción: "))
     if opcion <=0 or opcion >6:
        return opcion
     else:
        print("Ingrese un numero entre el 1 y el 6")     
        exit()
    except ValueError:
       print("Ingrese un numero")
       exit()

