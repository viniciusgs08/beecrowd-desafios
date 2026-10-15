print("=== CALCULADORA DE IMC ===")
nome = input("Ola, qual é o seu nome?: ")
print(

    f"{nome}. sou um sistema que esta em desenvolvimento"
    "APROVEITE ESSA VERSÃO TESTE LOGO LOGO EM HTML!!"

)

peso = float(input("Digite seu peso em Kg: "))
altura = float(input("Digite sua altura em metros: "))

if peso <= 0 or altura <= 0:
    print("Peso ou altura invalidos!:")

else:
    imc = peso / (altura ** 2)

    print(f"\nSeu IMC é: {imc:.2f}")

    if imc < 18.5:
        classificacao = "abaixo do peso"
    elif imc < 25:
        classificacao = "peso normal"
    elif imc < 30:
        classificacao = "sobrepeso"
    else:
        classificacao = "obesidade"

    print(f"Classificação: {classificacao}")

    print("\nVocê tem alguma duvida sobre essa classificação?")
    duvida = input("Digite sim ou não: ").strip().lower()

    if duvida == "sim":
        print("\nEscolha a classificação que corresponde a você: ")
        print("1 - Abaixo do peso")
        print("2 - Peso normal")
        print("3 - Sobrepeso")
        print("4 - Obesidade")

        escolha = input("Digite o numero correspondente: ")

        if escolha == "1":
            classificacao = "abaixo do peso"
        elif escolha == "2":
            classificacao = "Peso normal"
        elif escolha == "3":
            classificacao = "sobrepeso"
        elif escolha == "4":
            classificacao = "obsedidade"
        else:
            classificacao = "inválida"
    print("\n=== EXPLICAÇÃO E ORIENTAÇÕES ===")

    if classificacao == "abaixo do peso":
        print("Seu IMC está na faixa abaixo do peso.")
        print("Possíveis causas incluem alimentação insuficiente.")
        print("O ideal é avaliar sua saúde com um profissional.")
        print("Dica: mantenha refeições regulares e variadas.")

    elif classificacao == "peso normal":
        print("Seu IMC está na faixa considerada normal para adultos.")
        print("Continue cuidando da sua saúde.")
        print("Dica: consuma frutas, verduras, legumes e proteínas.")
        print("Pratique atividades físicas adequadas à sua rotina.")

    elif classificacao == "sobrepeso":
        print("Seu IMC está na faixa de sobrepeso.")
        print("O IMC sozinho não determina sua saúde.")
        print("Dica: priorize alimentos naturais e refeições equilibradas.")
        print("Tente caminhar regularmente, respeitando seus limites.")

    elif classificacao == "obesidade":
        print("Seu IMC está na faixa de obesidade.")
        print("Isso não é um diagnóstico completo de saúde.")
        print("Dica: procure orientação de um profissional de saúde.")
        print("Comece com hábitos sustentáveis, sem dietas extremas.")

    else:
        print("Opção inválida. Execute novamente e escolha de 1 a 4.")

    print("\n=== OBRIGADO POR TESTA O MEU PRIMEIRO PROJETO"
                         "CALCULO DE IMC."
          )