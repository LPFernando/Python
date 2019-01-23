#-*- coding: utf-8 -*-

import sys
#from test.test_readline import readline

agenda={}
lista=[]
intentos=3

def menu():
    
    print("        selecciona una opcion: ")
    print("        1. Añadir contacto.")
    print("        2. Buscar contacto.")
    print("        3. Eliminar contacto.")
    print("        4. Salir.")
    print("    *****************************")
    
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def funcion1(nombre):
    
    if nombre in agenda:
        
        return True
    
    else:
        
        return False
    
    
def funcion2(numero):
    
    if (int(numero/100000000)==9):
        
        return True
    
    else:
        
        return False
            
        
def Op1():
    
    NomUsuario=input("ingrese su nombre: ")
    NumUsuario=int(input("ingrese su numero: "))
    verificaNom=funcion1(NomUsuario)
    verificaNum=funcion2(NumUsuario)
    
    if len(str(NumUsuario))==9 and verificaNom==False and verificaNum==True:
        
        agenda[NomUsuario]=NumUsuario
        
        print("CONTACTO INSERTADO")
        
    else:
        
        print("NOMBRE O NUMERO INVALIDO")
        
#*****************************************************************************
def funcion3(subnombre):
    
    lista1=[]
    
    for elemento in agenda.keys():
        
        lista1.append(elemento)
        

    for elemento in lista1:
        
        if (subnombre in elemento):
            lista.append(elemento)
            
    if len(lista)>=1:
        
        return True
    
    else:
        
        return False
            
def Op2():
    
        nombre=input("ingrese nombre de contacto a buscar: ")
        
        sugerencia=funcion3(nombre)
        
        if (nombre in agenda):
            
            print("Contacto: "+nombre+" Numero: "+str(agenda.get(nombre)))
            
        elif (nombre in agenda)==False and sugerencia:
            
            print("Sugerencias de contactos:")
            print(lista)
            lista.clear()
            Op2()
            
        else:
            
            print("Contacto no existe en agenda")
        
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
def Op3():
    
    if len(agenda)>=1:
        
        ElimUsuario=input("Ingrese nombre de contacto a eliminar: ")
        del agenda[ElimUsuario]
        print("CONTACTO ELIMINADO")
        
    else:
        
        print("AGENDA ESTA VACIA")

#********************************************************************************

while intentos!=0:
    
    try:
        print("    ****************************")
        print("    *****    MI AGENDA    ******")
        menu()
    
        opMenu=int(input("Inserta numero de opcion: "))
    
        if opMenu==1:
            
            Op1()
            
        elif opMenu==2:
            
            Op2()
            
        elif opMenu==3:
            
            Op3()
            
        elif opMenu==4:
            
            print("Cerraste Programa")
            sys.exit() #break
            
        else:
            
            print("Opcion no valida, Usted tiene "+str(intentos-1)+" intentos")
            intentos-=1
            
            if  (intentos==0):
                
                print("Agotaste numero de intentos!!")
            
    except ValueError:
        
        print("Usted no ha ingresado un numero!!!")
    
