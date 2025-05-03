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
    for i in range(len(faces) - 4):
        if (faces[i] + 1 == faces[i+1] and
            faces[i] + 2 == faces[i+2] and
            faces[i] + 3 == faces[i+3] and
            faces[i] + 4 == faces[i+4]):
            return 30
    return 0

def calcula_pontos_full_house(faces):
    dicio = {}
    for i in faces:
        if i in dicio:
            dicio[i] += 1
        else:
            dicio[i] = 1
    valores = dicio.values()
    if sorted(valores) == [2, 3]:
        soma = 0
        for i in range(len(faces)):
            soma += faces[i]
        return soma
    return 0

def calcula_pontos_quadra(faces):
    dicio = {}
    for i in faces:
        if i in dicio:
            dicio[i] += 1
        else:
            dicio[i] = 1
    for qnt in dicio.values():
        if qnt >= 4:
            soma = 0
            for i in range(len(faces)):
                soma += faces[i]
            return soma
    return 0

def calcula_pontos_quina(faces):
    dicio = {}
    for i in faces:
        if i in dicio:
            dicio[i] += 1
        else:
            dicio[i] = 1
    for qnt in dicio.values():
        if qnt >= 5:
            return 50
    return 0

def calcula_pontos_regra_avancada(faces):
    cinco_iguais = calcula_pontos_quina(faces)
    full_house = calcula_pontos_full_house(faces)
    quadra = calcula_pontos_quadra(faces)
    sem_combinacao = calcula_pontos_soma(faces)
    sequencia_alta = calcula_pontos_sequencia_alta(faces)
    sequencia_baixa = calcula_pontos_sequencia_baixa(faces)
    return {
        'cinco_iguais': cinco_iguais,
        'full_house': full_house,
        'quadra': quadra,
        'sem_combinacao': sem_combinacao,
        'sequencia_alta': sequencia_alta,
        'sequencia_baixa': sequencia_baixa
    }

def faz_jogada(faces, cat, cartela):
    simples = calcula_pontos_regra_simples(faces)
    avancada = calcula_pontos_regra_avancada(faces)
    if cat.isdigit():
        catint = int(cat)
        cartela["regra_simples"][catint] = simples[catint]
    else:
        cartela["regra_avancada"][cat] = avancada[cat]
    return cartela
