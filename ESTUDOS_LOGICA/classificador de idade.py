#classificador de idade

idade = int(input("Qual é sua idade"))

if idade < 0:
    print("nota invalida")
elif idade <= 12:
    print("Criança")
elif idade <= 17:
    print("Adolecente")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")