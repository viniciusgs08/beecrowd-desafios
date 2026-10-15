#calculador de fret

compra = float(input("DIGITE O VALOR DA COMPRA"))

if compra < 0:
    print("Valor invalido")
elif compra < 100:
    print("Frete é de 20 reais")
elif compra < 200:
    print("Frete de 10 reais")
else:
    print("FRETE GRÁTIS")