from funcoes import *

cartela = {
    "regra_simples": {i: -1 for i in range(1, 7)},
    "regra_avancada": {
        'cinco_iguais': -1,
        'full_house': -1,
        'quadra': -1,
        'sem_combinacao': -1,
        'sequencia_alta': -1,
        'sequencia_baixa': -1
    }
}

rodada = 1
while rodada <= 12:
    print(f"\nRodada {rodada}")
    dados_rolados = rolar_dados(5)
    dados_guardados = []
    rerrolagens = 0

    while True:
        print(f"Dados rolados: {dados_rolados}")
        print(f"Dados guardados: {dados_guardados}")
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        opcao = input()

        if opcao == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input())
            if 0 <= indice < len(dados_rolados):
                resultado = guardar_dado(dados_rolados, dados_guardados, indice)
                dados_rolados, dados_guardados = resultado[0], resultado[1]
            else:
                print("Índice inválido.")

        elif opcao == "2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input())
            if 0 <= indice < len(dados_guardados):
                resultado = remover_dado(dados_rolados, dados_guardados, indice)
                dados_rolados, dados_guardados = resultado[0], resultado[1]
            else:
                print("Índice inválido.")

        elif opcao == "3":
            if rerrolagens < 2:
                dados_rolados = rolar_dados(len(dados_rolados))
                rerrolagens += 1
            else:
                print("Você já usou todas as rerrolagens.")

        elif opcao == "4":
            imprime_cartela(cartela)

        elif opcao == "0":
            print("Digite a combinação desejada:")
            combinacao = input()

            if combinacao.isdigit():
                comb_int = int(combinacao)
                if comb_int in cartela["regra_simples"]:
                    if cartela["regra_simples"][comb_int] == -1:
                        cartela = faz_jogada(dados_guardados + dados_rolados, combinacao, cartela)
                        break
                    else:
                        print("Essa combinação já foi utilizada.")
                else:
                    print("Combinação inválida. Tente novamente.")

            elif combinacao in cartela["regra_avancada"]:
                if cartela["regra_avancada"][combinacao] == -1:
                    cartela = faz_jogada(dados_guardados + dados_rolados, combinacao, cartela)
                    break
                else:
                    print("Essa combinação já foi utilizada.")
            else:
                print("Combinação inválida. Tente novamente.")

        else:
            print("Opção inválida. Tente novamente.")

    rodada += 1

imprime_cartela(cartela)

pontos_finais = 0
pontos_simples = 0

for valor in cartela["regra_simples"].values():
    if valor != -1:
        pontos_finais += valor
        pontos_simples += valor

for valor in cartela["regra_avancada"].values():
    if valor != -1:
        pontos_finais += valor

if pontos_simples >= 63:
    pontos_finais += 35
    print("Bônus de 35 pontos aplicado!")

print(f"Pontuação total: {pontos_finais}")