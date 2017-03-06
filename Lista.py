class NodoLista:
    def __init__(self,indice,nombre):
        self.nombre=nombre
        self.indice=indice
        self.siguiente=None

class Lista:
    def __init__(self):
        self.primero=None

    def insertar(self,index,dato):
        if self.primero==None:
            nuevo=NodoLista(index,dato)
            self.primero=nuevo
            nuevo.siguiente=None
        else:
            auxiliar=self.primero
            while auxiliar.siguiente!=None:
                auxiliar=auxiliar.siguiente
            nuevo=NodoLista(index,dato)
            auxiliar.siguiente=nuevo
    
    def buscar(self,nombre):
        respuesta="no existe ningun elemento con ese nombre"
        auxiliar=self.primero
        while auxiliar!=None:
            if auxiliar.nombre==nombre:
                respuesta="USUARIO EN LA POSICION "+auxiliar.indice
            auxiliar=auxiliar.siguiente
        
        return respuesta
    
    def Borrar(self,indice):
        if self.primero!=None:
            if self.primero.indice==indice and self.primero.siguiente==None:
                self.primero=None
            elif self.primero.indice==indice:
                self.primero=primero.siguiente
            else:
                anterior=self.primero
                temporal=self.primero.siguiente
                while temporal!=None and temporal.indice!=indice:
                    anterior=anterior.siguiente
                    temporal=temporal.siguiente
                if temporal!=None:
                    anterior.siguiente=temporal.siguiente
