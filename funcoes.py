import random

def rolar_dados(qnt):
    lista = []
    i = 0
    while i < qnt:
        x = random.randint(1, 6)
        lista.append(x)
        i += 1
    return lista

def guardar_dado(rolados, guardados, indice):
    listar = []
    listag = []
    for i in range(len(rolados)):
        listar.append(rolados[i])
    for i in range(len(guardados)):
        listag.append(guardados[i])
    listag.append(rolados[indice])
    del listar[indice]
    lista = []
    lista.append(listar)
    lista.append(listag)
    return lista

def remover_dado(rolados, guardados, indice):
    listar = []
    listag = []
    for i in range(len(rolados)):
        listar.append(rolados[i])
    for i in range(len(guardados)):
        listag.append(guardados[i])
    listar.append(guardados[indice])
    del listag[indice]
    lista = []
    lista.append(listar)
    lista.append(listag)
    return lista

def calcula_pontos_regra_simples(faces):
    dicio = {}
    i = 1
    while i <= 6:
        dicio[i] = 0
        i += 1
    for i in faces:
        dicio[i] += i
    return dicio

def calcula_pontos_soma(faces):
    s = 0
    for i in faces:
        s += i
    return s

def calcula_pontos_sequencia_baixa(faces):
    faces = sorted(set(faces))
    for i in range(len(faces) - 3):
        if (faces[i] + 1 == faces[i+1] and
            faces[i] + 2 == faces[i+2] and
            faces[i] + 3 == faces[i+3]):
            return 15
    return 0

def calcula_pontos_sequencia_alta(faces):
    faces = sorted(set(faces))
    for i in range(len(faces) - 3):
        if (faces[i] + 1 == faces[i+1] and
            faces[i] + 2 == faces[i+2] and
            faces[i] + 3 == faces[i+3] and
            faces[i] + 4 == faces[i+4]):
            return 30
    return 0