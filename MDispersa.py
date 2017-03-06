# -*- coding: utf-8 -*-
class NodoFila:
    def __init__(self,inicial):
        self.inicial=inicial
        self.abajo=None
        self.derecha=None
        self.indiceFila=0

class NodoColumna:
    def __init__(self,dominio):
        self.dominio=dominio
        self.derecha=None
        self.abajo=None
        self.indiceColumna=0


class NodoMatriz:
    def __init__(self,correo):
        self.correo=correo
        self.izquierda=None
        self.derecha=None
        self.abajo=None
        self.arriba=None
        self.adentro=None
        self.fila=0
        self.columna=0

class NodoProfundidad:
    def __init__(self,correo):
        self.correo=correo
        self.siguiente=None

class Matriz:
    def __init__(self):
        self.primeroFila=None
        self.primeroColumna=None

    def InsertarMatriz(self,datocorreo):
        existe1=False
        existe2=False
        existe3=False
        vector=datocorreo.split('@')
        cadena=vector[0]
        dominio=vector[1]
        dic=[["a",1],["b",2],["c",3],["d",4],["e",5],["f",6],
        ["g",7],["h",8],["i",9],["j",10],["k",11],["l",12],
        ["m",13],["n",14],["o",15],["p",16],["q",17],["r",18],
        ["s",19],["t",20],["u",21],["v",22],["w",23],["x",24],
        ["y",25],["z",26]]

        if self.primeroFila==None and self.primeroColumna==None:
            nf=NodoFila(cadena[0])
            nc=NodoColumna(dominio)
            nm=NodoMatriz(datocorreo)
            nf.derecha=nm
            nc.abajo=nm
            self.primeroFila=nf
            self.primeroColumna=nc
            for letra in dic:
                if letra[0]==cadena[0]:
                    fila=letra[1]
                    nf.indiceFila=fila
                    nm.fila=fila
                if letra[0]==dominio[0]:
                    columna=letra[1]
                    nm.columna=columna
                    nc.indiceColumna=columna

        else:
            auxiliar1=self.primeroFila
            while auxiliar1!=None:
                if auxiliar1.inicial==cadena[0]:
                    existe1=True
                auxiliar1=auxiliar1.abajo
            auxiliar2=self.primeroColumna
            while auxiliar2!=None:
                if auxiliar2.dominio==dominio:
                    existe2=True
                auxiliar2=auxiliar2.derecha

            nm=NodoMatriz(datocorreo)
            for letra in dic:
                if letra[0]==cadena[0]:
                    fila=letra[1]
                    nm.fila=fila
                if letra[0]==dominio[0]:
                    columna=letra[1]
                    nm.columna=columna

            if existe1==True:
                aux=self.primeroFila
                while aux!=None:
                    if aux.inicial==cadena[0]:
                        auxc=aux.derecha
                        while auxc!=None:
                            vector2=auxc.correo.split('@')
                            dominio2=vector2[1]
                            if dominio2==dominio:
                                existe3=True
                                if auxc.adentro==None:
                                    auxc.adentro=nm
                                else:
                                    auxprofundidad=auxc.adentro
                                    while auxprofundidad.adentro!=None:
                                        auxprofundidad=auxprofundidad.adentro
                                    auxprofundidad.adentro=nm

                            auxc=auxc.derecha

                    aux=aux.abajo
                if existe3==True:
                    pass
                else:
                    aux=self.primeroFila
                    while aux!=None:
                        if aux.inicial==cadena[0]:
                            if nm.columna<aux.derecha.columna:
                                nm.derecha=aux.derecha
                                aux.derecha.izquierda=nm
                                aux.derecha=nm
                            else:
                                auxiliar=aux.derecha
                                auxiliaratras=aux.derecha
                                while auxiliar.derecha!=None and nm.columna>=auxiliar.columna:
                                    auxiliaratras=auxiliar
                                    auxiliar=auxiliar.derecha
                                if nm.columna>=auxiliar.columna:
                                    auxiliar.derecha=nm
                                    nm.izquierda=auxiliar
                                else:
                                    auxiliaratras.derecha=nm
                                    nm.izquierda=auxiliaratras
                                    nm.derecha=auxiliar
                                    auxiliar.izquierda=nm

                        aux=aux.abajo
            else:
                nf=NodoFila(cadena[0])
                for let in dic:
                    if let[0]==cadena[0]:
                        indicef=let[1]
                        nf.indiceFila=indicef
                if nf.indiceFila<self.primeroFila.indiceFila:
                    nf.abajo=self.primeroFila
                    nf.derecha=nm
                    self.primeroFila=nf
                else:
                    auxiliar=self.primeroFila
                    auxiliaratras=self.primeroFila
                    while nf.indiceFila>=auxiliar.indiceFila and auxiliar.abajo!=None:
                        auxiliaratras=auxiliar
                        auxiliar=auxiliar.abajo
                    if nf.indiceFila>=auxiliar.indiceFila:
                        auxiliar.abajo=nf
                        nf.derecha=nm
                    else:
                        auxiliaratras.abajo=nf
                        nf.abajo=auxiliar
                        nf.derecha=nm
            if existe2==True:
                auxcolumna=self.primeroColumna
                while auxcolumna!=None:
                    if auxcolumna.dominio==dominio:
                        if nm.fila<auxcolumna.abajo.fila:
                            nm.abajo=auxcolumna.abajo
                            auxcolumna.abajo.arriba=nm
                            auxcolumna.abajo=nm
                        else:
                            temp=auxcolumna.abajo
                            tempatras=auxcolumna.abajo
                            while temp.abajo!=None and nm.fila>=temp.fila:
                                tempatras=temp
                                temp=temp.abajo
                            if nm.fila>=temp.fila:
                                temp.abajo=nm
                                nm.arriba=temp
                            else:
                                tempatras.abajo=nm
                                nm.abajo=temp
                                nm.arriba=tempatras
                                temp.arriba=nm
                    auxcolumna=auxcolumna.derecha
            else:
                nc=NodoColumna(dominio)
                for let in dic:
                    if let[0]==dominio[0]:
                        columna=let[1]
                        nc.indiceColumna=columna
                if nc.indiceColumna<self.primeroColumna.indiceColumna:
                    nc.derecha=self.primeroColumna
                    self.primeroColumna=nc
                    nc.abajo=nm
                else:
                    auxatras=self.primeroColumna
                    aux=self.primeroColumna
                    while aux.derecha!=None and nc.indiceColumna>=aux.indiceColumna:
                        auxatras=aux
                        aux=aux.derecha
                    if nc.indiceColumna>=aux.indiceColumna:
                        aux.derecha=nc
                        nc.abajo=nm
                    else:
                        auxatras.derecha=nc
                        nc.derecha=aux
                        nc.abajo=nm

    def BuscarLetra(self,letra):
        auxiliar=self.primeroFila
        listaletra=" "
        while auxiliar!=None:
            if letra==auxiliar.inicial:
                auxiliar2=auxiliar.derecha
                while auxiliar2!=None:
                    listaletra+=auxiliar2.correo+"\n"
                    if auxiliar2.adentro!=None:
                        auxiliar3=auxiliar2.adentro
                        while auxiliar3.adentro!=None:
                            listaletra+=auxiliar3.correo+"\n"
                            auxiliar3=auxiliar3.adentro
                    auxiliar2=auxiliar2.derecha
            auxiliar=auxiliar.abajo
        return listaletra

    def BuscarDominio(self,dom):
        aux=self.primeroColumna
        concatenar=""
        while aux!=None:
            if aux.dominio==dom:
                aux2=aux.abajo
                while aux2!=None:
                    concatenar+=aux2.correo+"\n"
                    if aux2.adentro!=None:
                        aux3=aux2.adentro
                        while aux3.adentro!=None:
                            concatenar+=aux3.correo+"\n"
                            aux3=aux3.adentro
                    aux2=aux2.abajo
            aux=aux.derecha
        return concatenar





