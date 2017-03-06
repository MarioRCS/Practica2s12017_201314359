# Practica2s12017_201314359
from flask import Flask, request, Response
import Lista
import MDispersa
import Cola
import Pila
app = Flask("EDD_codigo_ejemplo")

#Ejemplo de una clase, todos los metodos de las clases deben de tener como parametro el "self", que es como el .this en Java
                   
            

lis=Lista.Lista()
m=MDispersa.Matriz()
col=Cola.Cola()
p=Pila.Pila()
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

@app.route('/metodoWeb4',methods=['POST'])

def hello4():
    parametro = str(request.form['dato'])
    
    m.InsertarMatriz(parametro)
    
@app.route('/metodoWeb5',methods=['POST'])

def hello5():
    parametro = str(request.form['dato'])
	#dato2 = str(request.form['dato2'])
    nombre=m.BuscarLetra(parametro)   
    #return "Hola " + str(parametro) + "!"
    return nombre

@app.route('/metodoWeb6',methods=['POST'])

def hello6():
    parametro = str(request.form['dato'])
	#dato2 = str(request.form['dato2'])
    nombre=m.BuscarDominio(parametro)   
    #return "Hola " + str(parametro) + "!"
    return nombre

@app.route('/metodoWeb7',methods=['POST'])
def hello7():
    parametro = str(request.form['dato'])
    col.Encolar(parametro)
 
@app.route('/metodoWeb8',methods=['POST'])
def hello8():
    parametro = str(request.form['dato'])
    parametro=col.Desencolar() 
   
    return parametro

@app.route('/metodoWeb9',methods=['POST'])
def hello9():
    parametro = str(request.form['dato'])
    p.push(parametro)
    
@app.route('/metodoWeb10',methods=['POST'])
def hello10():
    parametro = str(request.form['dato'])
    parametro=p.pop()
    return parametro

@app.route('/metodoWeb11',methods=['POST'])
def hello11():
    texto="digraph{"+"\n"
    parametro = str(request.form['dato'])
    parametro="C:/Users/Roberto/Desktop/texto.txt";
    outfile = open("C:/Users/Roberto/Desktop/texto.txt", 'w') 
    auxiliar=lis.primero
    while auxiliar!=None:
        texto+="l"+str (auxiliar.nombre)+str (auxiliar.indice)+'[label="'+str(auxiliar.nombre)+'"]; \n'
        auxiliar=auxiliar.siguiente
    auxiliar2=lis.primero
    
    while auxiliar2.siguiente!=None:
        texto+="l"+str (auxiliar2.nombre)+str (auxiliar2.indice)+" -> "+"l"+str (auxiliar2.siguiente.nombre)+str (auxiliar2.siguiente.indice)+"; \n"
        auxiliar2=auxiliar2.siguiente
    texto+="}"
    outfile.write(texto)
    outfile.close()
    #parametro="reporte Generado Exitosamente"
    return parametro

@app.route('/metodoWeb12',methods=['POST'])
def hello12():
    texto="digraph{"+"\n"
    parametro = str(request.form['dato'])
    parametro="C:/Users/Roberto/Desktop/texto2.txt";
    outfile = open("C:/Users/Roberto/Desktop/texto2.txt", 'w') 
    auxiliar=col.primero
    while auxiliar!=None:
        texto+="c"+str (auxiliar.dato)+'[label="'+str(auxiliar.dato)+'"]; \n'
        auxiliar=auxiliar.siguiente
    auxiliar2=col.primero
    
    while auxiliar2.siguiente!=None:
        texto+="c"+str (auxiliar2.dato)+" -> "+"c"+str (auxiliar2.siguiente.dato)+"; \n"
        auxiliar2=auxiliar2.siguiente
    texto+="}"
    outfile.write(texto)
    outfile.close()
    #parametro="reporte Generado Exitosamente"
    return parametro

@app.route('/metodoWeb13',methods=['POST'])
def hello13():
    texto="digraph{"+"\n"
    parametro = str(request.form['dato'])
    parametro="C:/Users/Roberto/Desktop/texto3.txt";
    outfile = open("C:/Users/Roberto/Desktop/texto3.txt", 'w') 
    auxiliar=p.primero
    while auxiliar!=None:
        texto+="p"+str (auxiliar.dato)+'[label="'+str(auxiliar.dato)+'"]; \n'
        auxiliar=auxiliar.siguiente
    auxiliar2=p.primero
    
    while auxiliar2.siguiente!=None:
        texto+="p"+str (auxiliar2.dato)+" -> "+"p"+str (auxiliar2.siguiente.dato)+"; \n"
        auxiliar2=auxiliar2.siguiente
    texto+="}"
    outfile.write(texto)
    outfile.close()
    #parametro="reporte Generado Exitosamente"
    return parametro

@app.route('/metodoWeb15',methods=['POST'])
def hello15():
    texto="digraph{"+"\n"+"node [shape=box];"+"\n"
    parametro = str(request.form['dato'])
    regreso="C:/Users/Roberto/Desktop/texto5.txt";
    outfile = open("C:/Users/Roberto/Desktop/texto5.txt", 'w') 
    auxiliar=m.primeroFila
    while auxiliar!=None:
            if parametro==auxiliar.inicial:
                auxiliar2=auxiliar.derecha
                while auxiliar2!=None:
                    ident=auxiliar2.correo.split('@')
                    cadena=ident[0]
                    dominio=ident[1]
                    vector=dominio.split('.')
                    texto+=str(cadena)+str(vector[0])+'[label="'+str(auxiliar2.correo)+'"]; \n'
                    if auxiliar2.adentro!=None:
                        auxiliar3=auxiliar2.adentro
                        while auxiliar3!=None:
                            profundo=auxiliar3.correo.split('@')
                            cadena1=profundo[0]
                            dominio1=profundo[1]
                            vector1=dominio1.split('.')
                            texto+=str(cadena1)+str(vector1[0])+'[label="'+str(auxiliar3.correo)+'"]; \n'
                            auxiliar3=auxiliar3.adentro
                    auxiliar2=auxiliar2.derecha
            auxiliar=auxiliar.abajo
    
    aux=m.primeroFila
    while aux!=None:
            if parametro==aux.inicial:
                aux2=aux.derecha
                while aux2.derecha!=None:
                    ident=aux2.correo.split('@')
                    cadena=ident[0]
                    dominio=ident[1]
                    vector=dominio.split('.')
                    ident2=aux2.derecha.correo.split('@')
                    cadena2=ident2[0]
                    dominio2=ident2[1]
                    vector2=dominio2.split('.')
                    texto+=str(cadena)+str(vector[0])+" -> " +str(cadena2)+str(vector2[0])+"; \n"
                    if aux2.adentro!=None:
                        vadentro=aux2.correo.split('@')
                        nom=vadentro[0]
                        dom=vadentro[1]
                        union=dom.split('.')
                        
                        vadentro2=aux2.adentro.correo.split('@')
                        nom2=vadentro2[0]
                        dom2=vadentro2[1]
                        union2=dom2.split('.')
                        texto+=str(nom)+str(union[0])+" -> "+str(nom2)+str(union2[0])+"; \n"
                        aux3=aux2.adentro
                        while aux3.adentro!=None:
                            profundo=aux3.correo.split('@')
                            cadena1=profundo[0]
                            dominio1=profundo[1]
                            vector1=dominio1.split('.')
                            profundo2=aux3.adentro.split('@')
                            cadena3=profundo2[0]
                            dominio3=profundo2[1]
                            vector3=dominio3.split('.')
                            texto+=str(cadena1)+str(vector1[0])+" -> "+str(cadena3)+str(vector3[0])+"; \n"
                            aux3=aux3.adentro
                    aux2=aux2.derecha
            aux=aux.abajo
    
    
    texto+="}"
    outfile.write(texto)
    outfile.close()
    #parametro="reporte Generado Exitosamente"
    return regreso

@app.route('/metodoWeb16',methods=['POST'])
def hello16():
    texto="digraph{"+"\n"+"node [shape=box];"+"\n"
    parametro = str(request.form['dato'])
    regreso="C:/Users/Roberto/Desktop/texto6.txt";
    outfile = open("C:/Users/Roberto/Desktop/texto6.txt", 'w') 
    auxiliar=m.primeroColumna
    while auxiliar!=None:
            if parametro==auxiliar.dominio:
                auxiliar2=auxiliar.abajo
                while auxiliar2!=None:
                    ident=auxiliar2.correo.split('@')
                    cadena=ident[0]
                    dominio=ident[1]
                    vector=dominio.split('.')
                    texto+=str(cadena)+str(vector[0])+'[label="'+str(auxiliar2.correo)+'"]; \n'
                    if auxiliar2.adentro!=None:
                        auxiliar3=auxiliar2.adentro
                        while auxiliar3!=None:
                            profundo=auxiliar3.correo.split('@')
                            cadena1=profundo[0]
                            dominio1=profundo[1]
                            vector1=dominio1.split('.')
                            texto+=str(cadena1)+str(vector1[0])+'[label="'+str(auxiliar3.correo)+'"]; \n'
                            auxiliar3=auxiliar3.adentro
                    auxiliar2=auxiliar2.abajo
            auxiliar=auxiliar.derecha
    
    aux=m.primeroColumna
    while aux!=None:
            if parametro==aux.dominio:
                aux2=aux.abajo
                while aux2.abajo!=None:
                    ident=aux2.correo.split('@')
                    cadena=ident[0]
                    dominio=ident[1]
                    vector=dominio.split('.')
                    ident2=aux2.abajo.correo.split('@')
                    cadena2=ident2[0]
                    dominio2=ident2[1]
                    vector2=dominio2.split('.')
                    texto+=str(cadena)+str(vector[0])+" -> " +str(cadena2)+str(vector2[0])+"; \n"
                    if aux2.adentro!=None:
                        vadentro=aux2.correo.split('@')
                        nom=vadentro[0]
                        dom=vadentro[1]
                        union=dom.split('.')
                        
                        vadentro2=aux2.adentro.correo.split('@')
                        nom2=vadentro2[0]
                        dom2=vadentro2[1]
                        union2=dom2.split('.')
                        texto+=str(nom)+str(union[0])+" -> "+str(nom2)+str(union2[0])+"; \n"
                        aux3=aux2.adentro
                        while aux3.adentro!=None:
                            profundo=aux3.correo.split('@')
                            cadena1=profundo[0]
                            dominio1=profundo[1]
                            vector1=dominio1.split('.')
                            profundo2=aux3.adentro.split('@')
                            cadena3=profundo2[0]
                            dominio3=profundo2[1]
                            vector3=dominio3.split('.')
                            texto+=str(cadena1)+str(vector1[0])+" -> "+str(cadena3)+str(vector3[0])+"; \n"
                            aux3=aux3.adentro
                    aux2=aux2.abajo
            aux=aux.derecha
    
    
    texto+="}"
    outfile.write(texto)
    outfile.close()
    #parametro="reporte Generado Exitosamente"
    return regreso

@app.route("/e")  

def hellof():
    return "Hello World2!"
        

if __name__ == "__main__":
        app.run(debug=True, host='127.0.0.9')
