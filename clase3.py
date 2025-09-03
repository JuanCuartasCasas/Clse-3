
##El marcador 
#declaracion de variables
xp=0
xf=21
def ejercicio1():
    precio= float(input("Bienvenido,ingrese la cantidad de dinero en pesos  usada: "))
    if(precio >50000):
        print(f"Al invertir {precio} pesos,obtuvo un 5% de descuento en su proxima compra")
    elif(precio>80000):
        print(f"Muchas gracias por invertir {precio} pesos en nuestra tienda,obtuvo un 8% de descuento en su proxima compra")
    elif(precio>100000):
        print(f"!FELICIDADES! muchas gracias por invertir {precio} pesos en nuestra tienda,como beneficio obtuvo un 10% de descuento en su proxima compra")
    else:
        print(f"Muchas gracias por invertir {precio} pesos en nuestra tienda")


def multiplos(m):    
    for x in range(xp,xf,1):#recorrera de 0 a 4;parametros 
        if(x % m == 0):
            print(f"es multiplo de {m} el numero {x}")#f strings,buscar
        else:        
            print(f"No es multiplo de {m} el numero {x}")

def prueba():
    boleano = str(5* 3)    
    print(type(boleano),boleano)

def actividad():
    print("Listado de personas")
    for i in range(6):
        nombre = str(input("Ingrese su nombre: "))
        carrera = str(input("Ingrese la carrera que estudia: "))
        idea = str(input("Cual es su idea de proyecto para el curso: "))
        print(f"!!Hola {nombre} mucho gusto!!.Super interesante tu idea acerca de '{idea}'.Espero que te vaya muy bien estudiando {carrera}")

def main():
    #multiplos(5)
    #match()
    actividad()

if __name__ == "__main__":
    main()