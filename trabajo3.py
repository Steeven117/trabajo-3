# Verificar si un numero es positivo y de cuatro digitos.

print("-----------------------------------------------------------------")
print("-----------¿EL NUMERO ES POSITIVO Y DE CUATRO DIGITOS?-------------")
print("-----------------------------------------------------------------")

#input

A=int(input("Digite el valor de A: "))
Z=A
#Procesing

if A>0 : 
    rta = " el numero es positivo"

else:
    rta = " el numero no es positivo"


if   9999>=Z>=1000 :
    rt = " eL numero es de 4 digitos"

else:
    rt = " el numero no es de 4 digitos"


# OUTPUT

print(  str(rta))
print(  str(rt))