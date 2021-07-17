# Isaias Rafael Sandoya Vargas 
# Software
# #Tercer semestre

#clase Lunes 12 de julio 

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

ejer = ejercicios ()
num = int ( input ( "ingrese un numero:" ))
imprimir ( "llamada 1" )
ejer . perfecto ( num )
entrada ()
lista  = [ 3 , 5 , 6 , 8 , 28 ]
imprimir ( "llamada 2" )
para  num  en  lista :
     ejer . perfecto ( num )
entrada ()
imprimir ( "llamada 3" )
ejer . perfecto ( 23 )



############################################################################################################################################################################################################################################################################################ ###
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
                acu = acu + 1
        volver  acu


ejer = ejercicios ()
num = int ( input ( "ingrese un numero:" ))
imprimir ( "llamada 1" )
resp  =  ejer . perfecto2 ( num )
si  num  ==  resp :
    print ( "{} es perfecto" . formato ( número ))
otra cosa :
    print ( "{} no es perfecto" . formato ( número ))
  
# aporte()
# lista = [3,5,6,8,28]
# print ("llamada 2")
# para num en lista:
# ejer.perfecto (num)
# aporte()
# print ("llamada 3")
# ejer.perfecto (23)



############################################################################################################################################################################################################################################################################################ ###
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
                acu = acu + 1
        volver  acu


ejer = ejercicios ()
lista  = [ 3 , 5 , 6 , 8 , 28 ]
imprimir ( "llamada 2" )
perfectos = []
para  num  en  lista :
    si  ejer . perfecto2 ( num ) ==  num :
       perfecto . añadir ( num )
imprimir ( perfectos )
