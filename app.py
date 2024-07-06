from funciones import *
import json

continuar = True
nombre_incorrecto = True
bandera_carga_archivo = False
bandera_estadisticas = False
campo = "followers"


while continuar:

    menu()
    opcion = input("Ingrese la opción deseada: ")

    match opcion:
        case "1":
            while nombre_incorrecto:
                nombre_archivo = input("Ingrese el nombre del archivo a cargar o presione N para volver al menu: ")
                if nombre_archivo == "N":
                    break
                try:
                    with open(get_path_actual(nombre_archivo), "r", encoding="utf-8") as archivo:
                        encabezado = archivo.readline().strip("\n").split(",")

                        lineas = archivo.readlines()

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
                        espacio()
                    bandera_carga_archivo = True
                    break
                except:
                    print("El nombre del archivo es incorrecto o no existe. Por favor intente de nuevo.")
                    espacio()
        case "2":
                if bandera_carga_archivo:
                    mostrar_posteos(lista_posts)
                else:
                    print("Primero debe ingresar un archivo")
                    espacio()
        case "3":
                if bandera_carga_archivo:
                    lista_posts = mapear_lista(lista_posts)
                    bandera_estadisticas = True
                    print("Las estadisticas se cargaron con éxito")
                    espacio()
                else:
                    print("Primero debe ingresar un archivo")
                    espacio()
        case "4":
                if bandera_carga_archivo:
                    if bandera_estadisticas:
                        mejores_posteos = filtrar_mejores_posteos(lista_posts)

                        with open(get_path_actual("mejores_posts.csv"),"w", encoding="utf-8") as archivo:
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

                        print("Se filtraron los mejores post. Podes encontrarlos en el archivo mejores_posts.csv")
                        espacio()
                    else:
                        print("Es necesario cargar estadisticas para obtener la información")
                        espacio()
                else:
                    print("Primero debe ingresar un archivo")
                    espacio()
        case "5":
                if bandera_carga_archivo:
                    if bandera_estadisticas:
                        filtrar_haters = filtrar_haters(lista_posts)  
                        with open(get_path_actual("haters_posts.csv"),"w", encoding="utf-8") as archivo:
                            encabezado = ",".join(list(filtrar_haters[0].keys())) + "\n"

                            archivo.write(encabezado)
                            
                            for post in filtrar_haters:
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
                        print("Se filtraron los posts con más haters. Podes encontrarlos en el archivo haters_posts.csv")
                        espacio()
                    else:
                        print("Es necesario cargar estadisticas para obtener la información")
                        espacio()
                else:
                    print("Primero debe ingresar un archivo")
                    espacio()

        case "6":
                if bandera_carga_archivo:
                    if bandera_estadisticas:
                        mostrar_promedio_campo(lista_posts,campo)
                    else:
                        print("Es necesario cargar estadisticas para obtener la información")
                        espacio()
                else:
                    print("Primero debe ingresar un archivo")
                    espacio()
        case "7":
                if bandera_carga_archivo:
                    if bandera_estadisticas:
                        ordenar_users_ascendente(lista_posts)

                        with open(
                            get_path_actual("user_ascendente.json"), "w", encoding="utf-8"
                        ) as archivo:
                            json.dump(lista_posts, archivo, indent=4)

                        print("Se ordenaron los datos por nombre de user ascendente. Podes encontrarlos en el archivo user_ascendente.json")
                        espacio()
                    else:
                        print("Es necesario cargar estadisticas para obtener la información")
                        espacio()
                else:
                    print("Primero debe ingresar un archivo")
                    espacio()

        case "8":
            if bandera_carga_archivo:
                if bandera_estadisticas:
                    user_popular= obtener_user_popular(lista_posts)
                    print(f"El user {user_popular["user"]} tiene el posteo más likeado con {user_popular["likes"]} likes")
                    espacio()
                else:
                    print("Es necesario cargar estadisticas para obtener la información")
                    espacio()
            else:
                    print("Primero debe ingresar un archivo")
                    espacio()

        case "9":
            print("Saliendo de la aplicación")
            espacio()
            continuar=False
        
        case _:
            print("La opción no es válida. Intenta de nuevo.")
            espacio()

print("Fin del programa")



