nome = input()
salario_fixo = float(input())
total_vendas = float(input())

total_receber = salario_fixo + (total_vendas * 0.15)

print(f"TOTAL = R$ {total_receber:.2f}")