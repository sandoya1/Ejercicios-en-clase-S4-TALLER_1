# Isaias Rafael Sandoya Vargas 
# Software
# #Tercer semestre


#Ejercicio en clase 28/06/2021.

class ordenar:
    def __init__(self,lista):
        self.lista=lista

    def recorrerElemento(self):
        for ele in self.lista:
            print(ele)

    def recorrerPosicion(self):
        for pos,ele in enumerate(self.lista):
            print(pos,ele)

lista =[2,3,1,5,8,10]
ord1 = ordenar(lista)
ord1.recorrerElemento()
ord1.recorrerPosicion()
