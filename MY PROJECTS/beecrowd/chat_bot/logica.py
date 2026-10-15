#proejto de saude analist.

#o projeto coleta informações pessoal e de saude, baseado nas informações de saude não estiver na media, calculamos, passamos a situação atual
#e orienta oque deve fazer etc. no final o objt e fazer um mine site com CSS e HTML, que consegue fazer uma analise real, com graficos e mostra a situação.
#dentro do site ainda tem uma serie de treinos e alimentção baseado nas informações pessoais e de saude.



#coleta de informações
nome = input("Olá, Como eu posso te chamar?:")
altura = float(input(f"{nome}. Qual é sua altura?: "))
peso = float(input(f"{nome}. poderia me informa seu peso?: "))
idade = int(input("por ultimo, quantos anos você tem? "))

#calculo do IMC
imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f}")

if imc <= 18.5:
    print("Você esta a baixo do peso")
else:
    if imc < 25:
        print("peso normal")
    else:
        if imc < 30:
            print("Sobrepeso")
        else:
            print("Obesidade")


