# Isaias Rafael Sandoya Vargas 
# Software
# #Tercer semestre

# for in cadena - in(tupla) – in[lista]
cvoc=0
frase = input("Ingrese frase a usar: ")
for car in frase:
    if car in ("a","e","i","o","u","A","E","I","O","U"):
        if car in ["A", "E", "I", "O", "U"]:
            continue
        else:
           cvoc = cvoc + 1
print("""Cantidad vocales:{}""".format(cvoc))

def vocales(frase):
    for car in frase:
        if car in ('a', 'e', 'i', 'o', 'u'):
            print(car)
oracion = input('Ingrese una oracion: ')
vocales(oracion.lower())
