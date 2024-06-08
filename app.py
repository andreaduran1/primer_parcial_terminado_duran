from funciones import *
import json

def menu()->str:
    print("\nMenu de opciones:")
    print("1. Cargar archivo CSV")
    print("2. Imprimir lista")
    print("3. Asignar estadisticas")  
    print("4. Filtrar por mejores posts")  
    print("5. Filtrar por haters")
    print("6. Informar promedio de followers")
    print("7. Ordenar los datos por nombre de user ascendente")
    print("8. Mostrar más popular")
    print("9. Salir\n")


def redes_app():
    while True:

        menu()
        aux = input("Ingrese la opción deseada: ")
        opcion = int(aux)

        match opcion:
            case 1:
                while True:
                    nombre_archivo = input("Ingrese el nombre del archivo a cargar: ")

                    try:
                        with open(get_path_actual(nombre_archivo), "r", encoding="utf-8") as archivo:
                            encabezado = archivo.readline().strip("\n").split(",")

                            lineas = archivo.readlines()
                            # esto lo puedo recorrer para armar el diccionario

                            lista_posts = []

                            for linea in lineas:
                                post = {}

                                linea = linea.strip("\n").split(",")

                                id, user, likes, dislikes, followers = linea
                                post["id"] = int(id)
                                post["user"] = user
                                post["likes"] = int(likes)
                                post["dislikes"] = int(dislikes)
                                post["followers"] = int(followers)
                                lista_posts.append(post)
                            print("El archivo se cargó con éxito")
                        break
                    except:
                        print("El nombre del archivo es incorrecto o no existe. Por favor intente de nuevo.")

            case 2:
                    mostrar_posteos(lista_posts)
            
            case 3:
                    lista_estadisticas = mapear_lista(lista_posts)

            case 4:
                    mejores_posteos = filtrar_lista(lambda post: post["likes"] > 2000, lista_estadisticas)

                    with open(get_path_actual("mejores_posteos.csv"),"w", encoding="utf-8") as archivo:
                        encabezado = ",".join(list(mejores_posteos[0].keys())) + "\n"

                        archivo.write(encabezado)
                        
                        for post in mejores_posteos:
                            values = list(post.values())
                            l = []

                            for value in values:
                                if isinstance(value, int):
                                    l.append(str(value))
                                elif isinstance(value, float):
                                    l.append(str(value))
                                else:
                                    l.append(value)
                                    
                            linea = ",".join(l) + "\n"
                            archivo.write(linea)

            case 5:
                    filtrar_haters = filtrar_lista(lambda post: post["dislikes"] > post["likes"], lista_estadisticas)          
                    with open(get_path_actual("haters.csv"),"w", encoding="utf-8") as archivo:
                        encabezado = ",".join(list(filtrar_haters[0].keys())) + "\n"
        
        

                        archivo.write(encabezado)
        
                        for user in filtrar_haters:
                            values = filtrar_haters(user.values())
                            l = []

                            for value in values:
                                if isinstance(value, int):
                                    l.append(str(value))
                                elif isinstance(value, float):
                                    l.append(str(value))
                                else:
                                    l.append(value)
                                    
                            linea = ",".join(l) + "\n"
                            archivo.write(linea)


            case 6:
                    campo = "followers"
                    promedio_campo(nueva_lista,campo)

            case 7:
                    ordenar_lista(lambda a, b: a["user"] > b["user"], lista_estadisticas)

                    with open(
                        get_path_actual("user_ascendente.json"), "w", encoding="utf-8"
                    ) as archivo:
                        json.dump(lista_estadisticas, archivo, indent=4)


            case 8:

                    user_popular= reduce_lista(lambda ant, act: act if ant['likes'] < act['likes'] else ant, lista_estadisticas1)
                    print(f"El user {user_popular["user"]} tiene el posteo más likeado con {user_popular["likes"]} likes")


            case 9:
                print("Saliendo de la aplicación")
                break
            
            case _:
                print("La opción no es válida. Intenta de nuevo.")

    print("Fin del programa")

redes_app()




