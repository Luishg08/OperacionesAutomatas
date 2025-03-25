from Modelos import Estado
from Modelos import Transicion
from Modelos import Estado
from Modelos import Transicion
class AFND:
    def __init__(self):
        self.estados = []
        self.alfabeto = ""
        self.estadoInicial = None
        self.estadoFinal = None
        self.transiciones = []
        self.contador = 0
        self.visitados = []


    def imprimirTransiciones(self):
        for i in range(len(self.transiciones)):
            print("Origen {0} - Destino {1} - Simbolo {2}".format(self.transiciones[i].origen.nombre,self.transiciones[i].destino.nombre,self.transiciones[i].simbolo))

    def setAlfabeto(self,alfabeto):
        self.alfabeto = alfabeto

    def obtenerEstado(self,origen):
        for i in range(len(self.estados)):
            if self.estados[i].nombre == origen:
                return self.estados[i]

    def modeloA(self,letra):
        estado1 = Estado.Estado(str(self.contador))
        self.contador+=1
        estado2 = Estado.Estado(str(self.contador))
        self.contador+=1
        self.estados.append(estado1.nombre)
        self.estados.append(estado2.nombre)
        transicion = Transicion.Transicion(estado1,estado2,letra)
        estado1.transiciones.append(estado2.nombre)
        self.transiciones.append(transicion)
        bloque = AFND()
        bloque.estadoInicial = estado1
        bloque.estadoFinal = estado2
        return bloque

    def asterisco(self,bloque):
        nuevoEstadoInicial = Estado.Estado(str(self.contador))
        self.contador+=1
        nuevoEstadoFinal = Estado.Estado(str(self.contador))
        self.contador+=1
        transicion1 = Transicion.Transicion(nuevoEstadoInicial,bloque.estadoInicial,'e')
        transicion2 = Transicion.Transicion(bloque.estadoFinal, nuevoEstadoFinal, 'e')
        transicion3 = Transicion.Transicion(nuevoEstadoInicial,nuevoEstadoFinal,'e')
        transicion4 = Transicion.Transicion(bloque.estadoFinal,bloque.estadoInicial,'e')
        nuevoEstadoInicial.transiciones.append(bloque.estadoInicial.nombre)
        bloque.estadoFinal.transiciones.append(nuevoEstadoFinal.nombre)
        nuevoEstadoInicial.transiciones.append(nuevoEstadoFinal.nombre)
        bloque.estadoFinal.transiciones.append(bloque.estadoInicial.nombre)
        self.estados.append(nuevoEstadoInicial.nombre)
        self.estados.append(nuevoEstadoFinal.nombre)
        self.transiciones.append(transicion1)
        self.transiciones.append(transicion2)
        self.transiciones.append(transicion3)
        self.transiciones.append(transicion4)
        bloque = AFND()
        bloque.estadoInicial = (nuevoEstadoInicial)
        bloque.estadoFinal = nuevoEstadoFinal
        return bloque

    def mas(self,bloque):
        nuevoEstadoInicial = Estado.Estado(str(self.contador))
        self.contador += 1
        nuevoEstadoFinal = Estado.Estado(str(self.contador))
        self.contador += 1
        transicion1 = Transicion.Transicion(nuevoEstadoInicial, bloque.estadoInicial, 'e')
        transicion2 = Transicion.Transicion(bloque.estadoFinal, nuevoEstadoFinal, 'e')
        transicion4 = Transicion.Transicion(bloque.estadoFinal, bloque.estadoInicial, 'e')
        nuevoEstadoInicial.transiciones.append(bloque.estadoInicial)
        bloque.estadoFinal.transiciones.append(nuevoEstadoFinal.nombre)
        bloque.estadoFinal.transiciones.append(bloque.estadoInicial.nombre)
        self.estados.append(nuevoEstadoInicial.nombre)
        self.estados.append(nuevoEstadoFinal.nombre)
        self.transiciones.append(transicion1)
        self.transiciones.append(transicion2)
        self.transiciones.append(transicion4)
        bloque = AFND()
        bloque.estadoInicial = (nuevoEstadoInicial)
        bloque.estadoFinal = nuevoEstadoFinal
        return bloque

    def concatenar(self, bloque1, bloque2):
        bloque2.estadoInicial.nombre = bloque1.estadoFinal.nombre
        bloque = AFND()
        bloque.estadoInicial = bloque1.estadoInicial
        bloque.estadoFinal = bloque2.estadoFinal
        return bloque
    
    def disyuncion(self,bloque1,bloque2):
        nuevoEstadoInicial = Estado.Estado(str(self.contador))
        self.contador += 1
        nuevoEstadoFinal = Estado.Estado(str(self.contador))
        self.contador+=1
        self.transiciones.append(Transicion.Transicion(nuevoEstadoInicial,bloque1.estadoInicial,'e'))
        self.transiciones.append( Transicion.Transicion(nuevoEstadoInicial,bloque2.estadoInicial,'e'))
        self.transiciones.append(Transicion.Transicion(bloque1.estadoFinal,nuevoEstadoFinal,'e'))
        self.transiciones.append(Transicion.Transicion(bloque2.estadoFinal,nuevoEstadoFinal,'e'))
        nuevoEstadoInicial.transiciones.append(bloque1.estadoInicial.nombre)
        nuevoEstadoInicial.transiciones.append(bloque2.estadoInicial.nombre)
        bloque1.estadoFinal.transiciones.append(nuevoEstadoFinal.nombre)
        bloque2.estadoFinal.transiciones.append(nuevoEstadoFinal.nombre)
        self.estados.append(nuevoEstadoInicial.nombre)
        self.estados.append(nuevoEstadoFinal.nombre)
        bloque = AFND()
        bloque.estadoInicial = nuevoEstadoInicial
        bloque.estadoFinal = nuevoEstadoFinal
        return bloque

    def RecorridoProfundidad(self, dato):  # dato es en que vertice empieza el recorrido
        if dato in self.visitados:
            return
        else:
            Estado = self.obtenerEstado(dato)
            if Estado != None:
                self.visitados.append(Estado.nombre)
                for dato in Estado.transiciones:
                    self.RecorridoProfundidad(dato)
    