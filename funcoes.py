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
