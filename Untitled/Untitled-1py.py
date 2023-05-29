velocidade = float(input("informe quantos km : "))

if  velocidade > 80:
    print("multado")
else:
    print("velocidade permitida")

print("sua velocidade foi: {:.2f}".format(velocidade))
