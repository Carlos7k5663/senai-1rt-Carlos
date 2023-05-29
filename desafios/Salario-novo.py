salario = int(input("Informe seu salario: "))

if salario >= 8250.00:
    aumento = (salario * 10)
    total = (aumento /100)
    Nsalario = (total + salario) 
    

else: 
    aumento = (salario * 15)
    total = (aumento /100)
    Nsalario = (total + salario) 
    




print(f"Seu novo salario sera {Nsalario}")