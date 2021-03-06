class NodoCola:

    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None


class Cola:

    def __init__(self):
        self.primero=None

    def Encolar(self,dato):
        if self.primero==None:
            nc=NodoCola(dato)
            self.primero=nc
        else:
            nc=NodoCola(dato)
            auxiliar=self.primero
            while auxiliar.siguiente!=None:
                auxiliar=auxiliar.siguiente
            auxiliar.siguiente=nc

    def Desencolar(self):
        borrado=""
        if self.primero==None:
            borrado+="La Cola esta Vacia"
        else:
            borrado+="dato Desencolado: "+str(self.primero.dato)
            self.primero=self.primero.siguiente
        return borrado

    def MostrarCola(self):
        muestra=""
        auxiliar=self.primero
        while auxiliar!=None:
            muestra+=str(auxiliar.dato)+"\n"
            auxiliar=auxiliar.siguiente
        return muestra

