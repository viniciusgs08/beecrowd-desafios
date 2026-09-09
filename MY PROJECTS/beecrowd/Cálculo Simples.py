linha1 = input().split()
cod1 = int(linha1[0])
qtd1 = int(linha1[1])
val1 = float(linha1[2])

linha2 = input().split()
cod2 = int(linha2[0])
qtd2 = int(linha2[1])
val2 = float(linha2[2])


total = (qtd1 * val1) + (qtd2 * val2)

print(f"VALOR A PAGAR: R$ {total:.2f}")