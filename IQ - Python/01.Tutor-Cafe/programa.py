#expresiones regulares

import re

teclado = input("Como dice la vaca?: ") #----
#globo = re.sub  .sub(r".", "-",teclado) #Muuu
globo = re.sub(r".", "-",teclado)
globo = "  " + globo
print("\n")

print(globo)
print("< " + teclado + " >")
print(globo)
print("   \\  ^__^")
print("    \\ (oo)\\_______     ")
print("      (__)\\\\      )\\/\\      ")
print("           ||----w| ")
print("           ||    ||")
print("-----------------------------------------------------")



#Ejemplo del uso de funciones
n = "INVestiGacion"
print(n.lower())


"""
print('inv' in n) #true
print(n.lower())
"""