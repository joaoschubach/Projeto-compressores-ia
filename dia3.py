"""

temperatura_celcius = int(input("digite a temperatura do compressor em celcius: "))

if temperatura_celcius < 70:
    print("operação normal")
elif temperatura_celcius >= 70 and temperatura_celcius < 90:
    print("ATENÇÃO - temperatura elevada")
elif temperatura_celcius >= 90 :
    print("ALARME - temperatura crítica")



#desafio 28
import math
import random
print("O computador está pensando entre 0 e 5, tente adivinhar qual é o número!")
num_computador =random.randint(0,5)
num_usuario = int(input("Digite um número entre 0 e 5: "))
if num_usuario == num_computador:
    print("Parabéns, você acertou!")
elif num_usuario>5 or num_usuario<0:
    print( num_usuario, "não é um número válido, tente novamente!")
else:
    print("Que pena, você errou! O número era", num_computador)

#desafio 29
velocidade = int(input("Digite a velocidade do carro em km/h: "))
if velocidade > 80:
    print("MULTADO! Você excedeu o limite de velocidade permitido que é de 80 km/h.")
    multa = (velocidade - 80) * 7
    print("Você deve pagar uma multa de R$", multa) 
else:
    print("Velocidade dentro do limite permitido.")

# desafio 30 loop while
print("O computador está pensando entre 0 e 5, tente adivinhar qual é o número!")
num_computador =random.randint(0,5)
while num_usuario != num_computador:
    num_usuario = int(input("Digite um número entre 0 e 5: "))
    if num_usuario == num_computador:
        print("Parabéns, você acertou!")
    elif num_usuario>5 or num_usuario<0:
        print( num_usuario, "não é um número válido, tente novamente!")
    else:
        print("Que pena, você errou! Tente novamente!")
"""

temperatura_celcius = int(input("digite a temperatura do compressor em celcius: "))

verificador = input("Gostaria de verificar a temperatura do compressor? (s/n): ")

while verificador.lower() == "s":
    if temperatura_celcius < 70:
        print("operação normal")
    elif temperatura_celcius >= 70 and temperatura_celcius < 90:
        print("ATENÇÃO - temperatura elevada")
    elif temperatura_celcius >= 90 :
        print("ALARME - temperatura crítica")
    verificador = input("Gostaria de verificar a temperatura do compressor novamente? (s/n): ")
print("Programa encerrado. Caso queira verificar a temperatura do compressor novamente, execute o programa mais uma vez.")
