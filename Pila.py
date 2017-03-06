# -*- coding: utf-8 -*-
class NodoPila:

    def __init__(self,dato):

        self.dato=dato
        self.siguiente=None

class Pila:

    def __init__(self):
        self.primero=None

    def push(self,dato):
        if self.primero==None:
            np=NodoPila(dato)
            self.primero=np
        else:
            np=NodoPila(dato)
            np.siguiente=self.primero
            self.primero=np

    def pop(self):
        borrado=""
        if self.primero==None:
            borrado+="la pila esta vacia"
        else:
            borrado+=str(self.primero.dato)+" "+"fue el dato borrado"
            self.primero=self.primero.siguiente
        return borrado

    def MostrarPila(self):
        datospila=""
        auxiliar=self.primero
        while auxiliar!=None:
            datospila+=str(auxiliar.dato)+"\n"
            auxiliar=auxiliar.siguiente
        return datospila
