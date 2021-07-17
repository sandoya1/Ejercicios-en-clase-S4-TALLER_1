#Nombre: Isaias Rafael Sandoya Vargas 
#3er semestre de Software A1
# ejercicio en clase 2021-07-09

class Ordenar:
    def __init__(self, lista):
        self.lista=lista
    
    def recorrerElemento(self):
        for ele in self.lista:
            print(ele)
            
    # def recorrerPosicion(self):
    #     for pos,ele in enumerate(self.lista):
    #         print(pos,ele)        
    
    def recorrErenumerate(self):
        for pos,ele in enumerate(self.lista):
            print(pos,ele)
            
    def recorrerRange(self):
        for pos in range(len(self.lista)):
            print(pos,self.lista[pos])
    
    def buscar(self,buscado):
        enc=False
        for pos,ele in enumerate(self.lista):
            if ele == buscado:
                enc=True
                break
        if enc == True:return pos    
        else:return -1
        
    def ordenarAsc(self):
        for pos in range(0,len(self.lista)):
            for sig in range(pos+1,len(self.lista)):
                if self.lista[pos] > self.lista[sig]:
                    aux = self.lista[pos]
                    self.lista[pos]=self.lista[sig]
                    self.lista[sig]=aux
                    
    def ordenaeDesc(self):
        for pos,ele in enumerate(self.lista):
            for sig in range(pos+1,len(self.lista)):
                if ele < self.lista[sig]:
                    aux = self.lista[pos]
                    self.lista[pos]=self.lista[sig]
                    self.lista[sig]=aux
        
    def primer(self):
        return self.lista[0]

    def primerEliminado(self):
        primer=self.lista[0]
        auxilista= []
        for pos in range(1,len(self.lista)):
            auxilista.append(self.lista[pos])
        self.lista=auxilista
        return primer  
      
    def primerEliminado2(self):
        primer=self.lista[0]
        self.lista=self.lista[1:]
        return primer    
    
    def ultimo(self):
        return self.lista[-1]  
    
    def ultimoEliminado(self):
        ultimo=self.lista[-1]
        auxilista= []
        for pos in range(0,len(self.lista)-1):
            auxilista.append(self.lista[pos])
        self.lista=auxilista
        return ultimo
                
    def ultimoEliminado2(self):
        ultimo=self.lista[-1]
        self.lista=self.lista[0:-1]
        return ultimo
    
    def insertar(self, num):
        self.ordenarAsc()
        auxlista=[]
        for pos,ele in enumerate(self.lista):
            if num < ele:
                auxlista.append(num)
                break
        self.lista=self.lista[0:pos]+auxlista+self.lista[pos:]

    def insertar2(self, num):
        self.ordenarAsc()
        auxlista=[]
        for pos,ele in enumerate(self.lista):
            if num < ele:
                break
        for i in range(pos):
            auxlista.append(self.lista[i])
        auxlista.append(num)
        for j in range(pos,len(self.lista)):
            auxlista.append(self.lista[j])
        self.lista=auxlista
        
    def insertarOrden(self,num):
        self.lista.append(num)
        self.ordenarAsc()
    
    def eliminar(self,num):
        enc=False
        for pos,ele in enumerate(self.lista):
            if num==ele:
                enc=True
                break
        if enc: self.lista=self.lista[0:pos]+self.lista[pos+1:]
        return enc    
               
                  
                            
lista=[2,3,8,10]
ord1= Ordenar(lista)
if ord1.eliminar(8)==True: print("el numero se elimino de la lista",ord1.lista)
else: print("el numero nose encuentra en la lista")
# print(ord1.insertar(5))
# print(ord1.lista)
# print(ord1.insertar2(5))
# print(ord1.lista)
# print(ord1.primerEliminado())
# print(ord1.lista)

# print("____________________")
# print(ord1.lista)
# print(ord1.primerEliminado2())
# print(ord1.lista)

# # print("____________________")
# # print(ord1.lista)
# # print(ord1.ultimoEliminado2())
# # print(ord1.lista)

# print("____________________")
# print(ord1.lista)
# print(ord1.ultimoEliminado())
# print(ord1.lista)


# print("Primer",ord1.primer())
# print("Segundo",ord1.ultimo())
# print("Normal", ord1.lista)
# ord1.ordenarAsc()
# print("Asc",ord1.lista)     
# ord1.ordenaeDesc()
# print("Des",ord1.lista)
