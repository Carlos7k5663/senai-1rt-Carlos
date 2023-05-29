def somar(a, b):
    return a + b
def multiplicar(a, b):
    return a * b
def encontrar_maior(a, b):
    return max(a, b)
def encontrar_menor(a, b):
    return min(a, b)
print("escreva dois valores")
valor1 = float(input("valor 1: "))
valor2 = float(input("valor 2: "))
print("a. somar")
print("b. multiplicar")
print("c. maior número")
print("d. menor número")
opcao = input("Escolha uma opção (a, b, c ou d): ")
if opcao == "a":
    resultado = somar(valor1, valor2)
    print("resultado da soma:", resultado)
elif opcao == "b":
    resultado = multiplicar(valor1, valor2)
    print("resultado da multiplicação:", resultado)
elif opcao == "c":
    resultado = encontrar_maior(valor1, valor2)
    print("maior número:", resultado)
elif opcao == "d":
    resultado = encontrar_menor(valor1, valor2)
    print("menor número:", resultado)
else:
    print("opção inválida!")