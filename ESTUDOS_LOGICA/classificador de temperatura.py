#classificador de temperatura

temp = float(input("QUAL É A TEMPERATURA?: "))

if temp < 15:
    print("Esta frio")
elif temp < 25:
    print("Clima agradável")
else:
    print("Está calor!")


#sistema de notas

idade = int(input("Qual é sua idade"))

if idade < 0:
    print("nota invalida")
elif idade >= 0 or idade <= 12:
    print("Criança")
elif idade >= 13 or idade <= 17:
    print("Adolecente")
elif idade >= 18 or idade <= 59:
    print("Adulto")
else:
    print("idoso")