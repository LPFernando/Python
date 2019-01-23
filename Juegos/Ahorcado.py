#-*- coding: utf-8 -*

from random import randint
#imagenes para mostrar
imagenes_ahorcado=['''
    
    +---+
    |   |
        |
        |
        |
        |
  =========''','''
    +---+
    |   |
    o   |
        |
        |
        |
  =========''','''
  
    +---+
    |   |
    o   |
    |   |
        |
        |
  =========''','''
  
    +---+
    |   |
    o   |
   /|   |
        |
        |
  =========''','''
  
    +---+
    |   |
    o   |
   /|\  |
        |
        |
  =========''','''
  
    +---+
    |   |
    o   |
   /|\  |
   /    |
        |
  =========''','''
  
    +---+
    |   |
    o   |
   /|\  |
   /\   |
        |
  ========='''
  ] 
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
        elif intento not in "abcdefghijklmnñopqrstuvwxyz":
            print("ingrese una letra")
        else:
            return intento
        
#***********************************************************************************

print("A H O R C A D O")

letras_correctas=""
letras_incorrectas=""

palabra_secreta=obtener_palabra_Aleatoria(palabras)
juego_terminado=False

while True:
    
    intento=obtener_intento(letras_correctas+letras_incorrectas)
    
    if intento in palabra_secreta:
        #print("adivinaste.....")
        letras_correctas=letras_correctas+intento
        encontrado_todas_las_palabras=True
        
        for i in range(len(palabra_secreta)):
            
            if palabra_secreta[i] not in letras_correctas:
                
                encontrado_todas_las_palabras=False
                break
            
        if encontrado_todas_las_palabras:
            print("¡Has acertado!, la palabra secreta es "+palabra_secreta+" ¡Has Ganado!")
            juego_terminado=True
    else:
        
        letras_incorrectas=letras_incorrectas+intento
        print("fallaste..")     
          
        if len(letras_incorrectas)==len(imagenes_ahorcado)-1:
            
            print("Has agotado tus intentos \n Despues de ",str(len(letras_incorrectas))," intentos")
            juego_terminado=True
            