"""
Rangos

For:
for iterador in elemento_iterable
   instrucciones
   
"""

#ejemplo 1
x = range(0,11)
for iterador in x:
   print(iterador)
   
#ejemplo 2
#contador = 0
for contador in range(0,21):
   print("Voy por el " + str(contador))

print("\n")   

#ejemplo 3:
print("############# TABLAS DE MULTIPLICAR #############")
numero_usuario = int(input("Dame un numero para generar la tabla de multiplicar: "))

if numero_usuario < 1:
   numero_usuario = 1

print(f"############# FOR - TABLAS DE MULTIPLICAR DEL {numero_usuario} #############")

for iterador in range(1,11):
   print(f"{numero_usuario} x {iterador} = {numero_usuario * iterador}")
else:
   print("Tabla finalizada")



"""
while
"""
#ejemplo 1:
print("\n")
print("Utilizacion del while")
contador = 1
while contador <= 10:
   print(f"Estoy en el: {contador}")
   contador += 1
     

print("\n")

#ejemplo 2:
print("########### WHILE - TABLA DE MULTIPLICAR ###########")

numero_usuario = int(input("Ingresa otro numero: "))

print(f"########### TABLA DE MULTIPLICAR DEL {numero_usuario} ###########")

contador = 1
while contador <= 20:
   print(f"{numero_usuario} x {contador} = {numero_usuario * contador}")
   contador+=1

# ----------------------------------------------------
print("\nEjercicio con rangos: \n")
#rango:
#utilizando el for
#contador = 1

print("\n(Usando el for) - Numeros pares: ")
cadenaFor = ""
for contador in range(1,201):
   if(contador % 2 == 0):
      cadenaFor += str(contador) + ", "

print(cadenaFor)

print("\n(Usando el while) - Numeros pares: ")
#utilizando el while
iterador = 1
cadenaWhile = ""
while iterador <= 200:
   if(iterador % 2 == 0):
      cadenaWhile += str(iterador) + ", "
   iterador += 1

print(cadenaWhile)


#Ejercicio 4:
print("\n(Usando el for) - Cuadrado de un numero: ")
cuadrado = ""
for i in range(11):
   operacion = i*i
   cuadrado += str(operacion) + ", " 

print(cuadrado)

print("\n(Usando el while) - Cuadrado de un numero: ")
cuadradoWhile = ""
contador = 1
while contador <= 15:
   operacion = contador*contador
   cuadradoWhile += str(operacion) + ", " 
   contador += 1

print(cuadradoWhile)


#ejercicio 5:
print("Ejercicio 5 - Rango entre dos numeros")
n1 = int(input("Ingresa el primer valor: "))
n2 = int(input("Ingresa el segundo valor: "))

mayor = 0
menor = 0
if n1 < n2:
   mayor = n2
   menor = n1
elif n1 > n2:
   mayor = n1
   menor = n2
elif n1 == n2:
   mayor = n2
   menor = n2

print("\nRango utilizando el for: ")
for i in range(menor, mayor+1):
   print(f"{i}, ")

print("\nRango utilizando el while: ")
iterador = menor
while iterador <= mayor:
   print(f"{iterador}", )
   iterador+=1


#ejericio 6
print("\n Ejercicio 6 - Tablas de multiplicar ")

#con el for:
print("\nUtilizando el for: ")
for i in range(1,11):
   print(f"##############Tabla del {i}##################")
   for j in range(1,11):
      print(f"{j} x {i} = {j*i}")

print("\nUtilizando el while: ")
a = 1
while a <= 10:
   print(f"##############Tabla del {a}##################")
   b=1
   while b <= 10:
      print(f"{b} x {a} = {b*a}")
      b+=1
   
   a+=1


"""
   | 1 2 ...
---+------------
 1 | 1 2
 2 | 2 4 ...
 
 
"""
