def area(largura, comprimento):
    terreno = largura * comprimento
    return terreno
largura = float(input("escreva a largura do terreno em metros: "))
comprimento = float(input("escreva o comprimento do terreno em metros: "))
terreno = area(largura, comprimento)
print("a area do terreno é:", terreno, "metros quadrados.")
