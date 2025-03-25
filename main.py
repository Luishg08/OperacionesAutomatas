from Modelos import AFND
from Modelos import Construccion
import re
import os
import json
automata = AFND.AFND()

rutaArchivo = './Autómata1.json'
#Obtener el objeto json del archivo
with open(rutaArchivo) as archivo:
    automata1 = json.load(archivo)

rutaArchivo = './Autómata2.json'
#Obtener el objeto json del archivo
with open(rutaArchivo) as archivo:
    automata2 = json.load(archivo)

"""rutaArchivo = './AutómataResultante.json'
#Obtener el objeto json del archivo
with open(rutaArchivo) as archivo:
    automataResultante = json.load(archivo)"""

AutomataResultante = Construccion.Interseccion(automata1,automata2)

#Construccion.graficarConJSon(automata1)

#AutomataResultante = Construccion.Inverso(automata1)

#Construccion.graficarConJSon(automataResultante)


























































#Ejemplos de expresiones regulares que se pueden ingresar
    #(a+aa)*(b+aa)(a+ab+aa)*
    #(b+ba)(a+ab+aa)*
    #(a+ab+aa)*
    #(a+aa)*(b+aa)
    #(a+aa)*(b+aa)(a+ab+aa)*

"""for bloque in bloques:
    if bloque == '(a+b)':
        nuevoBloque = automata.disyuncion(automata.modeloA('a'),automata.modeloA('b'))
        bloques[bloques.index(bloque)] = nuevoBloque
    elif bloque == '(a)':
        nuevoBloque = automata.modeloA('a')
        bloques[bloques.index(bloque)] = nuevoBloque
    elif bloque == '(b)':
        nuevoBloque = automata.modeloA('b')
        bloques[bloques.index(bloque)] = nuevoBloque
    elif bloque == '(a+ab)':
        nuevoBloque = automata.disyuncion(automata.modeloA('a'),automata.concatenar(automata.modeloA('a'),automata.modeloA('b')))
        bloques[bloques.index(bloque)] = nuevoBloque
    elif bloque == '(a+ba)':
        nuevoBloque = automata.disyuncion(automata.modeloA('a'),automata.concatenar(automata.modeloA('b'),automata.modeloA('a')))
        bloques[bloques.index(bloque)] = nuevoBloque
    elif bloque == '(a+bb)':
        nuevoBloque = automata.disyuncion(automata.modeloA('a'),automata.concatenar(automata.modeloA('b'),automata.modeloA('b')))
        bloques[bloques.index(bloque)] = nuevoBloque
    elif bloque == '(b+ab)':
        nuevoBloque = automata.disyuncion(automata.modeloA('b'),automata.concatenar(automata.modeloA('a'),automata.modeloA('b')))
        bloques[bloques.index(bloque)] = nuevoBloque
    elif bloque == '(b+ba)':
        nuevoBloque = automata.disyuncion(automata.modeloA('b'),automata.concatenar(automata.modeloA('b'),automata.modeloA('a')))
        bloques[bloques.index(bloque)] = nuevoBloque
    elif bloque == '(b+bb)':
        nuevoBloque = automata.disyuncion(automata.modeloA('b'),automata.concatenar(automata.modeloA('b'),automata.modeloA('b')))
        bloques[bloques.index(bloque)] = nuevoBloque
    elif bloque == '(ab)':
        nuevoBloque = automata.concatenar(automata.modeloA('a'),automata.modeloA('b'))
        bloques[bloques.index(bloque)] = nuevoBloque
    elif bloque == '(ba)':
        nuevoBloque = automata.concatenar(automata.modeloA('b'),automata.modeloA('a'))
        bloques[bloques.index(bloque)] = nuevoBloque
    elif bloque == '(bb)':
        nuevoBloque = automata.concatenar(automata.modeloA('b'),automata.modeloA('b'))
        bloques[bloques.index(bloque)] = nuevoBloque
    elif bloque == '(aa)':
        nuevoBloque = automata.concatenar(automata.modeloA('a'),automata.modeloA('a'))
        bloques[bloques.index(bloque)] = nuevoBloque
    elif bloque == '(a+aa)':
        nuevoBloque = automata.disyuncion(automata.modeloA('a'),automata.concatenar(automata.modeloA('a'),automata.modeloA('a')))
        bloques[bloques.index(bloque)] = nuevoBloque
    elif bloque == '(b+aa)':
        nuevoBloque = automata.disyuncion(automata.modeloA('b'),automata.concatenar(automata.modeloA('a'),automata.modeloA('a')))
        bloques[bloques.index(bloque)] = nuevoBloque
    elif bloque == '(a+ab+aa)':
        nuevoBloque = automata.disyuncion(automata.modeloA('a'),automata.disyuncion(automata.concatenar(automata.modeloA('a'),automata.modeloA('b')),automata.concatenar(automata.modeloA('a'),automata.modeloA('a'))))
        bloques[bloques.index(bloque)] = nuevoBloque


    


print(bloques)


for bloque in range(len(bloques)-1):
    if type(bloques[bloque]) == AFND.AFND:
        if bloques[bloque+1] == '*':
            nuevoBloque = automata.asterisco(bloques[bloque])
            bloques[bloque] = nuevoBloque
while '*' in bloques:
    bloques.remove('*')

while len(bloques) > 1:
    nuevoBloque = automata.concatenar(bloques[0],bloques[1])
    bloques[0] = nuevoBloque
    bloques.pop(1)

print(bloques)
Construccion.mostrarAFND(automata)
"""

###################################################

#Ejemplo para la expresión regular (a+(a*b)*)b
"""bloque1 = automata.modeloA('a') 
bloque2 = automata.asterisco(bloque1)
bloque3 = automata.concatenar(bloque2,automata.modeloA('b'))
bloque4 = automata.asterisco(bloque3)
bloqueaux = automata.modeloA('a')
bloque5 = automata.disyuncion(bloque4,bloqueaux)
bloquefinal = automata.concatenar(bloque5,automata.modeloA('b'))

automata.imprimirTransiciones()
Construccion.mostrarAFND(automata)
####################################################
"""



