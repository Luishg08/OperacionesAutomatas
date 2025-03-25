class Transicion:
    def __init__(self, origen, destino, simbolo):
        self.origen = origen
        self.destino = destino
        self.simbolo = simbolo

    def setOrigen(self,origen):
        self.origen = origen

    def setDestino(self,destino):
        self.destino = destino

    def setSimbolo(self,simbolo):
        self.simbolo = simbolo