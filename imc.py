print("Qual o seu peso?")
peso = float(input())
print("Digite a sua altura:")
altura = float(input())
imc = peso / (altura ** 2)

if imc <= 17:
    print("Seu peso é: {} e seu IMC {:5.2f}, você está muito abaixo do peso." .format(peso, imc))
elif 17 < imc <= 18.49:
    print("Seu peso é: {} e seu IMC {:5.2f}, você está abaixo do peso." .format(peso, imc))
elif 18.5 <= imc <= 24.99:
    print("Seu peso é: {} e seu IMC {:5.2f}, você está com o peso normal." .format(peso, imc))
elif 25 <= imc <= 29.99:
    print("Seu peso é: {} e seu IMC {:5.2f}, você está acima do peso." .format(peso, imc))
elif 30 <= imc <= 34.99:
    print("Seu peso é: {} e seu IMC {:5.2f}, você está com obesidade I." .format(peso, imc))
elif 35 <= imc <= 39.99:
    print("Seu peso é: {} e seu IMC {:5.2f}, você está com obesidade II (severa)." .format(peso, imc))
elif imc >= 40:
    print("Seu peso é: {} e seu IMC {:5.2f}, você está com obesidade III (mórbida)." .format(peso, imc))