"""
Expresiones regulares
Cómo dice la vaca? 

Ingresar por el teclado un texto 
"""
import re

teclado = input("Como dice la vaca?: ")
#expresion regular . osea cada caracter

globo = re.sub(r".", "-", teclado)
#globo = re.sub(r"d", "-", teclado)
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

print("\n")
print("\n")