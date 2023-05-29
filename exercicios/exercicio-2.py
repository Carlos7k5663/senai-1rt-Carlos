def contagem_regressiva(numero):
    if numero < 0:
        print("o numero deve ser positivo.")
        return
    while numero >= 0:
        print(numero)
        numero -= 1
numero_inicial = int(input("escreva um numero inteiro positivo: "))
contagem_regressiva(numero_inicial)