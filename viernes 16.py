#Isaias Rafael Sandoya Vargas 
# Software
# #Tercer semestre

#clase Viernes 16 de julio 

def  __init__ ( yo ):
    aprobar
 ejercicios de clase :
    def  __init__ ( yo ):
        aprobar

    def  parimpar ( yo , número ):
        si  numero  %  2  ==  0 :
            print ( "{} es par" . formato ( numero ))
        otra cosa :
            print ( "{} es inpar" . formato ( número ))

    def  perfecto ( yo , número ):
        acu = 0
        para  i  en el  rango ( 1 , numero ):
            si  numero  %  i  ==  0 :
                acu = acu + 1
        si  numero  ==  acu :
                print ( "{} es perfecto" . formato ( número ))
        otra cosa :
                print ( "{} no es perfecto" . formato ( número ))
    
    def  perfecto2 ( yo , número ):
        acu = 0
        para  i  en el  rango ( 1 , numero ):
            si  numero  %  i  ==  0 :
                acu = acu + i
        volver  acu

    def  divisores ( self , num ):
        cont = 1
        divisores = []
        mientras  cont <  num :
            rec =  num  %  cont
            si  rec == 0 :
                divisores . añadir ( cont )
            cont = cont + 1
        imprimir ( divisores )

clase  Programacion ( ejercicios ):
    def  __init__ ( yo ):
        aprobar

    def  divisores ( self , num ):
        divisores = []
        para  cont  en  rango ( 1 , num ):
            rec =  num  %  cont
            si  rec == 0 :
                divisores . añadir ( cont )
        devuelve  divisores


prog1 =  Programacion ()
div =  prog1 . divisores ( 6 )
lista = [ 1 , 2 ]
lista2 =  lista + div
imprimir ( lista2 )


# num = 6
# acumdivisor = prog1.perfecto2 (num)
# if acumdivisor == num:
# print (num, "es perfecto")
# demás:
# print (num, "no es perfecto")
# numeros = [3,6,24,28]
# perfectos = []
# para numero en numeros:
# if prog1.perfecto2 (numero) == numero:
# perfectos.append (numero)
# imprimir (perfectos)
