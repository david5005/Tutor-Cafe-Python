"""
(*)| 1 2 ... 20
----------------
 1 | 1 2 
 2 | 2 4 ...
 
 
"""
print("\n")
cadena = ""
operacion = "(*) |"                 #<-correccion con los espacios en blanco
cadena += "{: <6}".format(operacion)
for i in range(1,21):
    #cadena += str(i)
    cadena += ("{: <7}".format(i)) 

#impresion de la primera fila guia
print("-"*len(cadena))
print(cadena)
print("-"*len(cadena))

cadena2 = ""
for i in range(1,21):
    valor = "{: <4}| ".format(str(i))
    cadena2 += valor
    for j in range(1,21):
        num = i*j
        #num = i+j
        #num = round ((i/j),2)
        #num = i-j
        cadena2 += ("{: <7}".format(num)) 
    
    cadena2+="\n"

print(cadena2)
