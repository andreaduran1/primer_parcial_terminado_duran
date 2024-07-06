LIKES_MIN = 500
LIKES_MAX = 3000
DISLIKES_MIN= 300
DISLIKES_MAX = 3500
FOLLOWERS_MIN = 10000
FOLLOWERS_MAX = 20000

MAYOR_LIKES = 2000

def get_path_actual(nombre_archivo):
    """Recibe el nombre de el archivo que queremos cargar y lo busca dentro del directorio actual

    Args:
        nombre_archivo: Nombre del archivo csv a cargar

    """    
    import os

    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual,nombre_archivo)


def menu():
    """Imprime un menu de opciones
    """    
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

def espacio()->None:
    """Genera un espacio en blanco
    """    
    print("")

def validar_lista(lista: list) -> None:
    """Valida que el argumento ingresado sea una lista

    Args:
        lista (list): Recibe una lista

    Raises:
        TypeError: Si el argumento ingresado no es una lista.
    """    
    if not isinstance(lista, list):
        raise TypeError("Se esperaba una lista.")
    
def sumar_lista(lista: list) -> int:
    """Suma todos los elementos de una lista

    Args:
        lista (list): Recibe una lista

    Returns:
        int: El resultado de la sumatoria de todos los elementos de la lista
    """    
    suma = 0
    validar_lista(lista)
    for i in lista:
        suma += i

    return suma

def calcular_promedio(lista: list) -> float:
    """Calcula el promedio de los elementos de una lista

    Args:
        lista (list): Recibe una lista

    Returns:
        float: El resultado de la sumatoria de todos los elementos de la lista dividido por la cantidad de elementos de la lista
    """    
    validar_lista(lista)

    if len(lista) != 0:
        promedio = sumar_lista(lista) / len(lista)
        return promedio
    else:
        return "No se puede dividir por 0"


def mostrar_posteos(posteos: list) -> None:
    """Muestra los elementos(posts) de una lista

    Args:
        posteos (list): recibe una lista
    """
    validar_lista(posteos)

    print("         ***Lista de Posteos***             ") 
    print("    Id         User             Likes    Dislikes   Followers")
    print("----------------------------------------------------------------------")

    for i in range(len(posteos)):
        mostrar_post_item(posteos[i])


def mostrar_post_item(post: dict) -> None:
    """Muestra el elemento de un diccionario

    Args:
        post (dict): recibe un elemento de diccionario
    """    
    print(
        f"{post["id"]:>4} {post["user"]:>20}    {post["likes"]:>6}    {post["dislikes"]:8}   {post["followers"]:6}"
    )


def mapear_lista(lista:list)->list:
    """Mapea una lista generando una nueva lista

    Args:
        lista (list): Recibe una lista

    Returns:
        list: retorna una nueva lista
    """    
    from random import randint

    validar_lista(lista)

    lista_retorno = []
    
    for el in lista:
        post = {}
        likes = randint(LIKES_MIN,LIKES_MAX)
        dislikes = randint(DISLIKES_MIN,DISLIKES_MAX)
        followers = randint(FOLLOWERS_MIN,FOLLOWERS_MAX)

        post["id"] = (el["id"])
        post["user"]= (el["user"])
        post["likes"]= likes
        post["dislikes"] = dislikes
        post["followers"] = followers

        lista_retorno.append(post)

    return lista_retorno

def mapear_campo(lista:list, campo:str)->list:
    """Mapea una lista en base al campo ingresado, retornando una nueva lista

    Args:
        lista (list): recibe una lista
        campo (str): recibe el parametro que se quiere mapear en la lista

    Returns:
        list: retorna una nueva lista
    """    
    validar_lista(lista)
    lista_retorno = []

    for post in lista:
        lista_retorno.append(post[campo])

    return lista_retorno

def filtrar_lista(filtradora, lista: list)->list:
    """Retornando una nueva lista filtrada segun las condiciones de la funcion filtradora

    Args:
        filtradora: recibe una funcion filtradora
        lista (list): recibe una lista a filtrar

    Returns:
        list: retorna la lista filtrada
    """    
    validar_lista(lista)
    lista_filtrada = []
    for el in lista:
        if filtradora(el):
            lista_filtrada.append(el)
    return lista_filtrada


def mostrar_promedio_campo(lista:list, campo:str)->None:
    """Promedia en una lista solo los valores del campo ingresado como atributo

    Args:
        lista (list): recibe una lista
        campo (str): recibe el campo de la lista que se quiere promediar
    """    
    validar_lista(lista)
    resultado = mapear_campo(lista,campo)
        
    print(f"El promedio de {campo} es {calcular_promedio(resultado):.0f}")

def swap_lista(lista: list, i: int, j: int) -> None:
    """Realiza el cambio de lugar entre dos elementos de una listas segun el criterio de ordenamiento

    Args:
        lista (list): recibe una lista a ordenar
        i (int): el primer elemento a comparar
        j (int): el segundo elemento a comparar
    """    
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux


def reduce_lista(funcion, lista:list, valor_inicial:int = None)->int:
    """Ejecuta una funcion reductora sobre cada elemento de la lista, devolviendo como resultado un unico valor

    Args:
        funcion: funcion reductora a ejecutar en cada elemento de la lista.
        lista (list): lista de elementos a ser reducida.
        valor_inicial (int, optional): primer argumento en la primera llamada a funcion. Defaults to None.

    Raises:
        ValueError: Si la lista esta vacia.

    Returns:
        int: retorna un unico valor como resultado de aplicar la funcion reductora
    """
    tam = len(lista)
    if tam == 0:
        raise ValueError("Error. Lista vacia")
    
    if valor_inicial:
        ant = valor_inicial
        indice = 0
    else:
        ant = lista[0]
        indice = 1

    for act in lista[indice:]:
        ant = funcion(ant,act)
    
    return ant


def filtrar_mejores_posteos(lista:list)->list:
    """Recibe una lista y filtra los posteos con más de 2000 likes.

    Args:
        lista (list): lista con likes a filtrar

    Return:
        Retorna una lista filtrada
    """    
    return filtrar_lista(lambda post: post["likes"] > MAYOR_LIKES, lista)


def filtrar_haters(lista:list)->list:
    """Filtra los post donde la cantidad de dislikes es mayor que la de likes

    Args:
        lista (list): Lista con posts a filtrar

    Returns:
        list: Lista filtrada
    """    
    return filtrar_lista(lambda post: post["dislikes"] > post["likes"], lista) 


def ordenar_users_ascendente(lista: list) -> None:
    """Ordena alfabeticamente una lista de usuarios de forma ascendente (A-Z)

    Args:
        lista (list): recibe la lista a ordenar
    """    
    tam = len(lista)

    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if lista[i]['user'] > lista[j]['user']:
                swap_lista(lista, i, j)

def obtener_user_popular(lista:list):
    """Obtiene al usuario con más followers de una lista de posts

    Args:
        lista (list): Recibe la lista con posts para

    """    
    return reduce_lista(lambda ant, act: act if ant['likes'] < act['likes'] else ant, lista)