import time
import random
from collections import deque


def gerar_tabuleiro(n):
    return [[random.randint(0, 1) for _ in range(n)] for _ in range(n)]


def todas_ligadas(tabuleiro):
    return all(valor == 1 for linha in tabuleiro for valor in linha)


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


def transformar_em_tupla(tabuleiro):
    return tuple(tuple(linha) for linha in tabuleiro)


def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(linha)


def busca_largura(tabuleiro_inicial):
    n = len(tabuleiro_inicial)
    fila = deque()
    visitados = set()

    fila.append((tabuleiro_inicial, 0))
    visitados.add(transformar_em_tupla(tabuleiro_inicial))

    while fila:
        tabuleiro_atual, jogadas = fila.popleft()

        if todas_ligadas(tabuleiro_atual):
            return {
                "achou": True,
                "jogadas": jogadas,
                "visitados": len(visitados)
            }

        for i in range(n):
            for j in range(n):
                proximo_tabuleiro = fazer_jogada(tabuleiro_atual, i, j)
                estado = transformar_em_tupla(proximo_tabuleiro)

                if estado not in visitados:
                    visitados.add(estado)
                    fila.append((proximo_tabuleiro, jogadas + 1))

    return {
        "achou": False,
        "jogadas": None,
        "visitados": len(visitados)
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
    resultado = busca_largura(tabuleiro)
    fim = time.time()

    print("\nResultado:")
    print("Achou solução:", resultado["achou"])
    print("Quantidade de jogadas:", resultado["jogadas"])
    print("Estados visitados:", resultado["visitados"])
    print("Tempo:", round((fim - inicio) * 1000, 2), "ms")