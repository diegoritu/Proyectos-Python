

#import math as m   #Importo la librería Math, pero la voy a usar como "m"

#from math import sqrt, pow

#Prueba con Input:
"""
print ("Introduzca un valor")
a= input()
print ("Introduzca otro valor")
b= input()
a= int(a)
b= int(b)
c=a+b
"""
#repr() pasa de int a String para mostrarlo
"""
print("El resultado de la suma es: " + repr(c))
"""
#If - Else: 
"""
if(c<10):
    print("El resultado es menor a 10")
else:
    print("El resultado es mayor o igual a 10")
"""



#todas las sentencias if/while deben llevar dos puntos y deben respetar la sangría
#While:
"""
if(c>=2):
    d=0
    while(c > d*3):
        d = c*a + d
        c = a+1
    print("Esto es d: " + repr(d))
"""

#For
"""for i in range(11):
     print("HOLA")
"""

#Lista:
"""
numeros= [1000,20,30,40]
numeros.sort(reverse= True)
print(numeros)
"""

#Tupla:
"""
tupla= (10,15,20,25,10)
cant= tupla.count(10) #Devuelve cuántas veces aparece ese valor en la lista
print(cant)
"""

#Set:
"""
s= {20,2,15,4,5,16,167}
print(s)
"""

#Números Complejos
"""
a= 4
b= 2
c= complex(a,b)
print(c)
"""

#Booleanos
"""
booleano= True
print(booleano)
booleano= False
print(booleano)
"""

#Diccionarios
"""
vehiculosPersonal= {'Pepe':'Peugeot 405', 'Raul' : 'Peugeot 504', 'Jorge' : 'Toyota Corolla'}
print(vehiculosPersonal.keys())
print(vehiculosPersonal.values())
print('Auto de Raul: ' + vehiculosPersonal['Raul']) #En los Diccionarios no se busca por posición, sino por clave
print('Auto de Raul (Por Get): ' + vehiculosPersonal.get('Raul')) #Get es igual a []
"""

#Librería Math importándola como "m"
"""#Raíz cuadrada
print('Introduzca el número del que quiera calcular su raíz cuadrada: ')
inp= input()
x= m.sqrt(float(inp))
print('La raíz cuadrada de '+ inp + ' es: ' + repr(x))

f= m.floor(x) #Redondea para abajo
print('La raíz redondeada para abajo es: ' + repr(f))
c= m.ceil(x) #Redondea para arriba
print('La raíz redondeada para arriba es: ' + repr(c))

mp= m.pow(4,2) #4 elevado al cuadrado
print('Prueba de math.pow(4,2): ' + repr(mp))

pi= m.pi #Número Pi
print('Número Pi: '+ repr(pi))

epsilon= m.e #Número e
print('Número Epsilon (e): '+ repr(epsilon))
"""

"""x=pow(4,5)
print(repr(x))
x= sqrt(2)
print(repr(x))
"""

#LIBRERÍA NUMPY

from numpy import *
"""lin= linspace(0,100,5) # Crea un array de un inicio a un final dividiéndolo en 5 partes iguales
print(lin)

ar= arange(1,11,2)
# Crea un array de un inicio a un final cargándolo con datos de a 2 
# (arranca en 1 y va sumando de a 2 hasta llegar al elemento antes del 11)
print(ar)

log= logspace(0,100,5)

cer= zeros(3,int)
uns= ones(3,int)
print (cer)
print (uns)
"""
#Suma de vectores
"""arr1= array([1,2,3,12])
arr2= array([2,4,3,12])
arr1= arr1+arr2
print(arr1)
"""
#Copia Superficial de Arreglos
"""arr1= array([3,2,5,6,8])
print(id(arr1))
arr3Superficial= arr1.view()
print(arr3Superficial, id(arr3Superficial))
"""
#Copia Profunda de Arreglos
"""arr1= array([3,2,5,6,8])
print(id(arr1))
arr4Profundo= arr1.copy()
print(arr4Profundo, id(arr4Profundo))
"""




