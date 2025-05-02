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

print(guardar_dado([1, 3, 2], [1, 2], 1))