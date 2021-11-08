import math
import datetime

def calculadora(n1, n2):
    suma = n1 + n2
    resta = n1 - n2
    mult = n1 * n2
    div = n1 / n2
    print(f"La suma es: {suma}")
    print(f"La resta es: {resta}")
    print(f"La multiplicacion es: {mult}")
    print(f"La division es: {div}")

def saludar(nombre):
    print(f"Hola {nombre}, bienvenido al curso de Python")

#ejercicio comprobacion dia:
def comprobarDia(dia):
    if dia == 1:
        print("El dia es Lunes")
    elif dia == 2:
        print("El dia es Martes")
    elif dia == 3:
        print("El dia es Miercoles")
    elif dia == 4:
        print("El dia es Jueves")
    elif dia == 5:
        print("El dia es Viernes")
    elif dia == 6:
        print("El dia es Sabado")
    elif dia == 7:
        print("El dia es Domingo")

#ejercicio datetime:
def dayNow():
    fecha_completa = datetime.datetime.now()
    print(fecha_completa.year) # 2021
    print(fecha_completa.month) # 11
    print(fecha_completa.day) #8
    fecha_Personalizada = fecha_completa.strftime("%d/%m/%Y")
    print(f"La fecha actual es: {fecha_Personalizada}")


#ejercicio 3a
def ejercicio3a(n):
    raiz = math.sqrt(n)
    print(f"Raiz cuadrada de {n} es {raiz}") #3.0
    print(f"Raiz cuadrada de {n} es", (int)(raiz)) #3


#ejercicio 3b
def ejercicio3b(n2):
    print("Uso de math ceil, floor: (1)------------------------------------------------")
    print("--redondear: ", math.ceil(n2)) #7
    print("--redondear: ", math.floor(n2)) # 6


#ejercicio 4
def ejercicio4(pais):
    if (pais != "Mexico" and pais != "El Salvador" and pais != "Cuba" and pais !="Venezuela" and pais != "Ecuador"):
        print(f"{pais} NO es un pais de habla hispana")
    else:
        print(f"{pais} es un pais de habla hispana")


#ejercicio 5
def ejercicio5(nombre, ciudad, continente, edad, mayoria_edad):
    if edad >= mayoria_edad:
        print(f"{nombre} es mayor de edad")
        
        if continente != "Europa":
            print("El usuario NO es europeo")
        else:
            print(f"El usuario es europeo y de {ciudad}")
    else:
        print(f"{nombre} NO es mayor de edad")







#------
#-- Comentarios solo para recordar, todo lo que quitamos del codigo principal y hacerlo mas compacto
"""
pais = "Alemania"

if(pais == "Mexico" or pais == "Ecuador" or pais == "Cuba" or pais == "Venezuela" or pais == "EL Salvador"):
    print(f"{pais} es un pais de habla hispana")
else:
    print(f"{pais} NO es un pais de habla hispana")

print("Ejercicio 4: (2)------------------------------------------------")

if not (pais == "Mexico" or pais == "Ecuador" or pais == "Cuba" or pais == "Venezuela" or pais == "El Salvador"):
    print(f"{pais} NO es un pais de habla hispana")
else:
    print(f"{pais} es un pais de habla hispana")
    
print("Ejercicio 4: (3)------------------------------------------------")
if (pais != "Mexico" and pais != "El Salvador" and pais != "Cuba" and pais !="Venezuela" and pais != "Ecuador"):
    print(f"{pais} NO es un pais de habla hispana")
else:
    print(f"{pais} es un pais de habla hispana")
print("------------------------------------------------")
"""


#-----------------------------------
"""
Ejercicio 5
nombre = "Juan"
ciudad = "Barcelona"
continente = "Europa"
edad = 18
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad")
    
    if continente != "Europa":
        print("El usuario NO es europeo")
    else:
        print(f"El usuario es europeo y de {ciudad}")
else:
    print(f"{nombre} NO es mayor de edad")


#------

currentTime = datetime.datetime.now()
date = currentTime.date()
year = date.strftime("%Y")
print(f"Current year: {year}")

day = date.strftime("%A")
print(f"Current day: {day}")
"""

"""
if dia>=1 and dia<=7: 
    if dia == 1:
        print("El dia equivale al Lunes")
    else:
        if dia == 2:
            print("El dia equivale al Martes")
        else:
            if dia == 3:
                print("El dia equivale al Miercoles")
            else:
                if dia == 4:
                    print("El dia equivale al Jueves")
                else:
                    if dia == 5:
                        print("El dia equivale al Viernes")
                    else:
                        if dia == 6:
                            print("El dia equivale al Sabado")
                        else:
                            print("El dia equivale al Domingo")
else:
    print("El numero debe estar entre el 1 al 7")

# ------------------------------------
"""