#classificador de Desempenho de aluno:

nota = float(input("DIGITE A NOTA: "))

if nota < 0 or nota > 10:
    print("NOTA INVÁLIDA")
elif nota < 4:
    print("DESEMPENHO INSUFICIENTE")
elif nota < 6:
    print("DESEMPENHO REGULAR")
elif nota < 8:
    print("BOM DESEMPENHO")
else:
    print("Exelente Desempenho")