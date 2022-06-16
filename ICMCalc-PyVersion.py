print("Olá vamos calcular seu IMC?")
altura = float(input("Insira sua altura, em metros:"))
peso = float(input("Insira seu peso: "))

imc = peso / (altura * altura)

if imc > 18.5 and imc < 25:
    print("Seu IMC é: {0:.2f}".format(imc))
    print("Você está dentro do seu peso ideal!")
if imc > 25:
    print("Seu IMC é: {0:.2f}".format(imc))
    print("Você está acima do seu peso ideal!")
if imc < 18.5:
    print("Seu IMC é: {0:.2f}".format(imc))
    print("Você está abaixo do seu peso ideal!")