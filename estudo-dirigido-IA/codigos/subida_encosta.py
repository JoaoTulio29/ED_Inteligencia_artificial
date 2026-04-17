import time
import random


def gerar_tabuleiro(n):
    return [[random.randint(0, 1) for _ in range(n)] for _ in range(n)]


def todas_ligadas(tabuleiro):
    return all(valor == 1 for linha in tabuleiro for valor in linha)


def contar_apagadas(tabuleiro):
    return sum(valor == 0 for linha in tabuleiro for valor in linha)


def copiar_tabuleiro(tabuleiro):
    return [linha[:] for linha in tabuleiro]


def fazer_jogada(tabuleiro, linha, coluna):
    n = len(tabuleiro)
    novo_tabuleiro = copiar_tabuleiro(tabuleiro)

    posicoes = [
        (linha, coluna),
        (linha - 1, coluna),
        (linha + 1, coluna),
        (linha, coluna - 1),
        (linha, coluna + 1)
    ]

    for x, y in posicoes:
        if 0 <= x < n and 0 <= y < n:
            novo_tabuleiro[x][y] = 1 - novo_tabuleiro[x][y]

    return novo_tabuleiro


def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(linha)


def subida_encosta(tabuleiro_inicial, limite_passos=1000):
    tabuleiro_atual = copiar_tabuleiro(tabuleiro_inicial)
    jogadas = 0
    visitados = 1

    while jogadas < limite_passos:
        if todas_ligadas(tabuleiro_atual):
            return {
                "achou": True,
                "jogadas": jogadas,
                "visitados": visitados
            }

        n = len(tabuleiro_atual)
        melhor_tabuleiro = tabuleiro_atual
        menor_qtd_apagadas = contar_apagadas(tabuleiro_atual)

        for i in range(n):
            for j in range(n):
                proximo_tabuleiro = fazer_jogada(tabuleiro_atual, i, j)
                qtd_apagadas = contar_apagadas(proximo_tabuleiro)
                visitados += 1

                if qtd_apagadas < menor_qtd_apagadas:
                    melhor_tabuleiro = proximo_tabuleiro
                    menor_qtd_apagadas = qtd_apagadas

        if menor_qtd_apagadas >= contar_apagadas(tabuleiro_atual):
            return {
                "achou": False,
                "jogadas": None,
                "visitados": visitados
            }

        tabuleiro_atual = melhor_tabuleiro
        jogadas += 1

    return {
        "achou": False,
        "jogadas": None,
        "visitados": visitados
    }


if __name__ == "__main__":
    n = 3
    tabuleiro = [
    [0, 1],
    [1, 0]
]

    print("Tabuleiro inicial:")
    mostrar_tabuleiro(tabuleiro)

    inicio = time.time()
    resultado = subida_encosta(tabuleiro)
    fim = time.time()

    print("\nResultado:")
    print("Achou solução:", resultado["achou"])
    print("Quantidade de jogadas:", resultado["jogadas"])
    print("Estados visitados:", resultado["visitados"])
    print("Tempo:", round((fim - inicio) * 1000, 2), "ms")