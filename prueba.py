from funciones import *

# import json

lista = [
    {"id": 1, "user": "lmalletratt0", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 2, "user": "skilmurray1", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 3, "user": "vhowgego2", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 4, "user": "mmcsporrin3", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 5, "user": "htacker4", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 6, "user": "bhutchence5", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 7, "user": "epetr6", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 8, "user": "pcucinotta7", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 9, "user": "mlumly8", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 10, "user": "mduerden9", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 11, "user": "bdurstona", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 12, "user": "acalcottb", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 13, "user": "hfenlonc", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 14, "user": "phigbind", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 15, "user": "dlabese", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 16, "user": "gpettettf", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 17, "user": "dgifkinsg", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 18, "user": "rrosewarneh", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 19, "user": "dmayoi", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 20, "user": "dgannanj", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 21, "user": "emulqueenk", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 22, "user": "amcgeel", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 23, "user": "zfurseym", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 24, "user": "asummersiden", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 25, "user": "hdaykino", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 26, "user": "pmingop", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 27, "user": "jlysterq", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 28, "user": "rkinghornr", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 29, "user": "gmerrgans", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 30, "user": "kdalgarnot", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 31, "user": "mmaxweellu", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 32, "user": "nthurlbeckv", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 33, "user": "scroalw", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 34, "user": "nlearnedx", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 35, "user": "cmarshamy", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 36, "user": "flagez", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 37, "user": "loates10", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 38, "user": "ayea11", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 39, "user": "jdeackes12", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 40, "user": "rworsley13", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 41, "user": "hdominetti14", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 42, "user": "kitzakovitz15", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 43, "user": "tpfeffer16", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 44, "user": "ojanu17", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 45, "user": "jdressell18", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 46, "user": "aferneyhough19", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 47, "user": "srowett1a", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 48, "user": "ahodgins1b", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 49, "user": "mboycott1c", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 50, "user": "lbarribal1d", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 51, "user": "jnorsworthy1e", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 52, "user": "scawse1f", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 53, "user": "jsaing1g", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 54, "user": "hnairns1h", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 55, "user": "ctabour1i", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 56, "user": "mtithecott1j", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 57, "user": "mchastaing1k", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 58, "user": "kmeineken1l", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 59, "user": "nkubicek1m", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 60, "user": "cburder1n", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 61, "user": "szupo1o", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 62, "user": "akemson1p", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 63, "user": "cgossling1q", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 64, "user": "snoller1r", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 65, "user": "cfriday1s", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 66, "user": "eantusch1t", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 67, "user": "chintzer1u", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 68, "user": "svasin1v", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 69, "user": "gletts1w", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 70, "user": "jjosefsen1x", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 71, "user": "tmckeaney1y", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 72, "user": "mlorden1z", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 73, "user": "cdmitrievski20", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 74, "user": "bmarcus21", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 75, "user": "agehringer22", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 76, "user": "mgerriet23", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 77, "user": "mlovatt24", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 78, "user": "pboyack25", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 79, "user": "kklemencic26", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 80, "user": "mvossgen27", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 81, "user": "lnorcliff28", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 82, "user": "rphilp29", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 83, "user": "wjeavon2a", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 84, "user": "skingston2b", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 85, "user": "fstollhofer2c", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 86, "user": "choggin2d", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 87, "user": "dkeilty2e", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 88, "user": "lholbarrow2f", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 89, "user": "cgrimsdell2g", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 90, "user": "malexis2h", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 91, "user": "wcluff2i", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 92, "user": "udubock2j", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 93, "user": "dgoracci2k", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 94, "user": "eearey2l", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 95, "user": "tquartermaine2m", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 96, "user": "lkabsch2n", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 97, "user": "gmacsharry2o", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 98, "user": "cdarkott2p", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 99, "user": "apetrecz2q", "likes": 0, "dislikes": 0, "followers": 0},
    {"id": 100, "user": "bgreser2r", "likes": 0, "dislikes": 0, "followers": 0},
]


# nueva_lista = mapear_lista(lista)
# print(type(nueva_lista))

# # mejores_posteos = filtrar_lista(lambda post: post["likes"] > 2000, nueva_lista)

# # mostrar_posteos(mejores_posteos)

# # filtrar_haters = filtrar_lista(lambda post: post["dislikes"] > post["likes"], nueva_lista)

# # mostrar_posteos(filtrar_haters)
# # campo = "followers"

# # promedio_campo(nueva_lista,campo)

# # ordena de mas pesado a mas liviano
# # ordenar_lista(lambda a, b: a["user"] > b["user"], nueva_lista)
# # mostrar_posteos(nueva_lista)


# # # para pasar a json
# # with open(
# #     get_path_actual("user_ascendente.json"), "w", encoding="utf-8"
# # ) as archivo:
# #     json.dump(nueva_lista, archivo, indent=4)

# user_popular= reduce_lista(lambda ant, act: act if ant['likes'] < act['likes'] else ant, nueva_lista)
# print(f"El user {user_popular["user"]} tiene el posteo más likeado con {user_popular["likes"]} likes")

mejores_posteos = filtrar_lista(lambda post: post["likes"] > 2000, lista)
with open(get_path_actual("personas_mayusculas.csv"),"w", encoding="utf-8") as archivo:
    encabezado = ",".join(list(lista[0].keys())) + "\n"
    
    # keys = list(lista[0].keys())
    # print(keys)
    # encabezado = ",".join(keys) + "\n"

    archivo.write(encabezado)
    
    for persona in lista:
        values = list(persona.values())
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