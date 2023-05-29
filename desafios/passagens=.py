distancia = float (input ("informe a distancia percorrida em km: "))

if distancia <= 200:
   aumento = (distancia *0.45)
else:
    aumento = (distancia *0.50)

    print(f"o valor total sera de {aumento}!")
    