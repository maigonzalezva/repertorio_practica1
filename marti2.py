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

