# Practica2s12017_201314359
from flask import Flask, request, Response
app = Flask("EDD_codigo_ejemplo")

#Ejemplo de una clase, todos los metodos de las clases deben de tener como parametro el "self", que es como el .this en Java
class Usuario():
    def __init__(self, password, correo, nombre):
        self.nombre = nombre
        self.password = password
        self.correo = correo
        

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
                    
                        
            

lis=Lista()
@app.route('/metodoWeb',methods=['POST'])

def hello():
    parametro = str(request.form['dato'])
    dato2 = str(request.form['dato2'])
    
    lis.insertar(dato2,parametro)
    
@app.route('/metodoWeb3',methods=['POST'])

def hello3():
    parametro = str(request.form['dato'])  
    lis.Borrar(parametro)
    

@app.route('/metodoWeb2',methods=['POST'])

def hello2():
    parametro = str(request.form['dato'])
	#dato2 = str(request.form['dato2'])
    nombre=lis.buscar(parametro)    
    #return "Hola " + str(parametro) + "!"
    return nombre

@app.route("/e")  

def hellof():
    return "Hello World2!"
        

if __name__ == "__main__":
        app.run(debug=True, host='127.0.0.9')
