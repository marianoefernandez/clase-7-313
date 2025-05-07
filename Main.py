#Los arreglos paralelos (listas paralelas) son arrays que guardan un conjunto de información especifico para un fin por ejemplo guardar los datos de los usuarios, vamos a usar cada array por cada dato del usuario y estos mismos se van a relacionar porque tienen el mismo indice.
#Los arrays paralelos tienen que tener la misma cantidad de elementos

#Legajo
#Nombre
#Edad
#Sueldo

from Funciones import *

#Tener 3 usuarios en mi sistema
lista_nombres = [0,0,0]
lista_legajos = [0,0,0]
lista_edades = [0,0,0]
lista_sueldos = [0,0,0]
bandera_carga = False

#La informacion la relacionamos mediante el indice

#Mostrar la informacion

#Menú

import os

saludar()

while True:
    print("1.Cargar Usuarios\n2.Mostrar Usuarios\n3.Mostrar promedio sueldos\n4.Mostrar el empleado con el salario más alto (SOLO UNO)\n5.Salir")
    opcion = int(input("Su opcion: "))
    while opcion > 5 or opcion < 1:
        opcion = int(input("Reingrese su opcion (1-5): "))
    
    if opcion == 1:
        respuesta = cargar_usuarios(lista_nombres,lista_edades,lista_legajos,lista_sueldos)
        if respuesta == True:
            print("PUDO CARGAR LOS USUARIOS")
            bandera_carga = True
        else:
            print("NO PUDO CARGAR LOS USUARIOS")
    elif opcion == 2:
        if bandera_carga == True:
            mostrar_usuarios(lista_nombres,lista_edades,lista_legajos,lista_sueldos)
        else:
            print("No hay usuarios cargados, no se puede mostrar los mismos")
    elif opcion == 3:
        if bandera_carga == True:
            suma_sueldos = sumar_sueldos(lista_sueldos)
            promedio_sueldo = calcular_promedio(suma_sueldos,len(lista_sueldos))
            print(f"El promedio de sueldos es : $ {promedio_sueldo}")
        else:
            print("No hay usuarios cargados, no se puede calcular el promedio")
    elif opcion == 4:
        if bandera_carga == True:
            print("USUARIO CON MAYOR SUELDO:")
            indice_usuario = buscar_usuario_mayor_salario(lista_sueldos)
            mostrar_usuario(lista_nombres,lista_edades,lista_legajos,lista_sueldos,indice_usuario)
        else:
            print("No hay usuarios cargados, no se puede calcular el mayor salario")
    elif opcion == 5:
        print("SALIENDO...")
        break
    input("Toque cualquier boton para continuar...")
    os.system("clear")