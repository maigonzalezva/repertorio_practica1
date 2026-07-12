

def sumar(numero4, numero2):
    suma = numero4+numero2
    return suma


numero3 = int(input("ingrese un numero: "))
numero1 = int(input("ingrese otro numero: "))

resultado = sumar(numero3, numero1)
print(resultado)

def validacion_duracion(duracion):
    try:
        duracion = int(duracion)
        if duracion > 0:
            return True
        else:
            return False
    except ValueError:
        return False
    
duracion = "1000"
    
resultado = validacion_duracion(duracion)
print(resultado)

def validacion_duracion(duracion):
    try:
        duracion = int(duracion)
        if duracion > 0:
            return True
        else:
            return False
    except ValueError:
        return False
    
duracion = "1000"
    
resultado = validacion_duracion(duracion)
print(resultado)

#ejercico opcion 1
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
