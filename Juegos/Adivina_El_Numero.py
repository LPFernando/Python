from random import randint
import sys

contador=0

nombre=input("Hola, Como te llamas? ")

numPensado=randint(1,20)
print("Bueno, ",nombre,", estoy pensando en un numero entre 1 y 20")

while contador<10:
    
    contador+=1
    
    print("Intenta adivinar")
    
    numero=int(input("Ingrese numero: "))

    if numero<=0:
        print("Numero no es correcto.")
        contador-=1
        
    elif numero>20:
        print("Numero muy grande")
        contador-=1
        
    else:
        
        if numPensado==numero:
            print("Buen trabajo",nombre," Has adivinado mi numero en ",contador," intentos")
            sys.exit()
            
        elif numPensado>numero:
            print("Tu estimacion es muy baja...")
            continue
            
        else:
            print("Tu estimacion es muy alta...")
            continue