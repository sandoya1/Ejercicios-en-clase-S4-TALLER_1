# Isaias Rafael Sandoya Vargas 
# Software
# #Tercer semestre


#taller en clases, ejercicios hechos por el maestro3
#Replica realizada por el estudiante

""" num =19
nombre= "rafa"
print(num,type(num))
print(nombre,type(nombre))
def mensaje(msg):
    print(msg)   
    
mensaje("Mi primer programa")
mensaje("Mi segundo programa") """

class sintaxis:
    instancia=0
     #__init__ Metodo constructor que se ejecuta cuando se instancia la clase cuyo objetivo es crear
     #e iniciar los atributos de la clase. self es un objetivo que representa la clase creada
    def __init__(self ,dato="llamando al constructor1"):
        self.frase=dato #atributo de instancia
        sintaxis.instancia = sintaxis.instancia+1
    
    def usoVariables(self):
        edad, _peso=23, 64.5
        nombres = 'Isaias Sandoya'
        Tipo_sexo = 'M'
        civil = True
        # tuplas = () son colecciones de datos de cualquier tipo inmutables
        usuario=()
        usuario=('isandoyav','236','isaias2019sandoya@gmail.com')
        # print(usuario[2],nombres[7])
        # #usuario[3] = "Jujan"
        # #lista = [] colecciones mutables
        materias=[]
        materias=['Programación Web','PHP','POO']
        aux=materias[1]
        materias[1]="python"
        materias.append("Go")
        #print(materias,aux, materias[1])
        
        # #diccionario = {} colecciones de objetos clave:valor tipo json
        docente={}
        docente = {'nombres':'Isaias','edad':19,'activo':True}
        edad=docente['edad']
        docente['edad']=20
        docente['carrera']='IS'
        # print(docente,edad,docente['edad'])
        # print(usuario,usuario[0], usuario[0:2],usuario[-1])
        # print(nombres,nombres[0], nombres[0:2],nombres[-1])
        print(materias,materias[2:],materias[:3], materias[::-1],materias[-2:])
        # #presentacion con format
        # print("""Mi nombre es {}, tengo {}
        #       años""".format(nombres,edad))
# print("sintaxis antes de instancia es: {}".format(sintaxis.instancia))        
ejer1=sintaxis() #instancia la clase sintaxis y crea el objeto ejer1(copia de la clase)
# print("sintaxis de ejer1 es: {}".format(sintaxis.instancia))
# ejer2=sintaxis("instancia2")
# print(ejer1.frase)
# print("sintaxis de ejer2 es: {}".format(sintaxis.instancia))
# print("sintaxis nuevamente ejer1 : {}".format(sintaxis.instancia))
# print(ejer2.frase)
ejer1.usoVariables()
