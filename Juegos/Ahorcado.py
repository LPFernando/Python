#-*- coding: utf-8 -*

from random import randint

#lista de palabras, gracias al metodo split

palabras = '''hormiga babuino tejon murcielago oso castor camello gato
almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro
rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra
nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte
salmon foca tiburon oveja mofeta perezoso serpiente araña cigüeña cisne tigre
sapo trucha pavo tortuga comadreja ballena lobo wombat cebra'''.split()

def obtener_palabra_Aleatoria(lista_De_palabras):
    
    indice_palabra=randint(0,len(lista_De_palabras)-1)
    return lista_De_palabras[indice_palabra]

def obtener_intento(letras_probadas):
    
    while True:#bucle infinito
        intento=input("Adivine una letra.").lower()
        if len(intento)!=1:
            print("Ingrese una letra, por favor.")
        elif intento in letras_probadas:
            print("Cambia de letra, por favor.")
        elif intento not in "abcdefghijklmn�opqrstuvwxyz":
            print("ingrese una letra")
        else:
            return intento

print("A H O R C A D O")

letras_correctas=""
letras_incorrectas=""

palabra_secreta=obtener_palabra_Aleatoria(palabras)
intento=obtener_intento(letras_correctas+letras_incorrectas)

if intento in palabra_secreta:
    print("adivinaste.....")
else:
    print("fallaste..")         