import random

def mostrar_usuarios(lista_nombres:list,lista_edades:list,lista_legajos:list,lista_sueldos:list) -> None:
    for i in range(len(lista_nombres)):
        print(f"MUESTRO USUARIO {i + 1}")
        mostrar_usuario(lista_nombres,lista_edades,lista_legajos,lista_sueldos,i)
        
def cargar_usuarios(lista_nombres:list,lista_edades:list,lista_legajos:list,lista_sueldos:list) -> bool:
    retorno = False 
    
    if type(lista_edades) == list and type(lista_nombres) == list and type(lista_legajos) == list and type(lista_sueldos) == list:
        for i in range(len(lista_nombres)):
            print(f"CARGANDO EL USUARIO {i + 1}")
            #Recuerden validar los mismos
            nombre_usuario = input("Ingrese el nombre: ")
            edad_usuario = int(input("Ingrese la edad: "))
            sueldo_usuario = float(input("Ingrese el sueldo: "))
            legajo_usuario = random.randint(11111,99999)
            
            lista_nombres[i] = nombre_usuario
            lista_legajos[i] = legajo_usuario
            lista_sueldos[i] = sueldo_usuario
            lista_edades[i] = edad_usuario
            
            #Si quieren mejorar la carga, podrian pedir una confirmacion al usuario en caso de que haya cargado algo mal
            print("USUARIO CARGADO CON EXITO")
            retorno = True
    return retorno

def sumar_sueldos(lista_sueldos:list) -> float:
    suma_sueldos = 0
    
    for i in range(len(lista_sueldos)):
        suma_sueldos += lista_sueldos[i]
    
    return suma_sueldos

def calcular_promedio(acumulador:float,contador:int) -> float | None:
    if contador != 0:
        #Puedo calcular el promedio
        promedio = acumulador / contador
    else:
        promedio = None
        
    return promedio

def buscar_usuario_mayor_salario(lista_sueldos:list) -> int:
    maximo = lista_sueldos[0]
    for i in range(len(lista_sueldos)):
        if lista_sueldos[i] > maximo:
            maximo = lista_sueldos[i]
            indice_usuario = i
                
    return indice_usuario

def mostrar_usuario(lista_nombres:list,lista_edades:list,lista_legajos:list,lista_sueldos:list,indice:int) -> None:
    print(f"Legajo: {lista_legajos[indice]}")
    print(f"Nombre: {lista_nombres[indice]}")
    print(f"Edad: {lista_edades[indice]} años")
    print(f"Sueldo: $ {lista_sueldos[indice]}")
    print("")
    
def saludar():
    print("HOLA MUNDO")