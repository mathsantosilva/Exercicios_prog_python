## Exercicios ChatGPT
## Regras: não utilize sort(), sorted(), max(), min() ou reverse(). Quero que você construa a lógica.
from os import cpu_count


def encontrar_extremos(numeros):
    if len(numeros) < 1:
        return None
    maior = numeros[0]
    menor = numeros[-1]
    for num in numeros:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    return  maior, menor


def mover_zeros(numeros):
    troca = True
    limite_reducao = 1
    while troca and limite_reducao < len(numeros):
        for num in range(len(numeros) - limite_reducao):
            if numeros[num] == 0:
                temp = numeros[num]
                numeros[num] = numeros[num + 1]
                numeros[num + 1] = temp
                troca = True
        limite_reducao += 1
    return  numeros

def ordenar_e_contar(numeros):
    troca = True
    limite_reducao = 1
    count = 0
    while troca and limite_reducao < len(numeros):
        for num in range(len(numeros) - limite_reducao):
            if numeros[num] > numeros[num + 1]:
                temp = numeros[num]
                numeros[num] = numeros[num + 1]
                numeros[num + 1] = temp
                troca = True
                count += 1
        limite_reducao += 1
    return  numeros, count

def segundo_maior(numeros):
    if len(numeros) < 1:
        return None
    maior = numeros[0]
    segundo_maior = None
    for num in numeros:
        if num > maior:
            segundo_maior = maior
            maior = num
        elif segundo_maior is not None:
            if num > segundo_maior and num < maior:
                segundo_maior = num
        elif segundo_maior is None and num < maior:
            segundo_maior = num

    return segundo_maior
