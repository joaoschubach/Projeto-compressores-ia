"""
import math
num = int(input("Digite um número: "))
raiz = math.sqrt(num)
print("A raiz quadrada de", num, "é:", raiz)

num2 = float(input("Digite outro número decimal: "))
print(num2, "arredondado para cima é:", math.ceil(num2))
print(num2, "sem a virgula é:", f"{num2:.0f}")

cateto_oposto = int(input("Digite o valor do cateto oposto de um triangulo retângulo: "))
cateto_adjacente = int(input("Digite o valor do cateto adjacente de um triangulo retângulo: "))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print("A hipotenusa do triangulo retângulo é:", hipotenusa)
print("O valor do cosseno do triangulo é:", math.cos(math.radians(hipotenusa)))
print("O valor do seno do triangulo é:", math.sin(math.radians(hipotenusa)))

frase = "Olá, sou João Araujo e vou construir uma ia de diagnóstico"
print(frase[0:3]) # Olá
print(frase[6:9]) # sou 
print(frase.count("á"))
print(frase.count("á"))
print(frase.count("a",0,15))
print(len(frase))

while True:
    n1 = int(input("Digite a temperatura do compressor em celcius: "))
    n2 = int(input("Digite a temperatura do compressor em celcius: "))
    n3 = int(input("Digite a temperatura do compressor em celcius: "))
    #compressor 1
    if n1 == n1.lowercase("sair"):
        break
    elif n1 < 70:
        print("operação normal")
    elif n1 >= 70 and n1 < 90:
        print("ATENÇÃO - temperatura elevada")
    elif n1 >= 90 :
        print("ALARME - temperatura crítica")
    if n2 == n2.lowercase("sair"):
        break
    elif n2 < 70:
        print("operação normal")
    elif n2 >= 70 and n2 < 90:
        print("ATENÇÃO - temperatura elevada")
    elif n2 >= 90 :
        print("ALARME - temperatura crítica")
    if n3 == n3.lowercase("sair"):
        break
    elif n3 < 70:
        print("operação normal")
    elif n3 >= 70 and n3 < 90:
        print("ATENÇÃO - temperatura elevada")
    elif n3 >= 90 :
        print("ALARME - temperatura crítica")   


n1= 89
n2= 0
n3= 4
temperatura_compressor = [n1,n2,n3]
print(temperatura_compressor)
temperatura_compressor.sort()
print(temperatura_compressor)
temperatura_compressor.sort(reverse=True)
print(temperatura_compressor)   
temperatura_compressor.append(100)
print(temperatura_compressor)
temperatura_compressor.insert(0,50)
print(temperatura_compressor)
temperatura_compressor.remove(100)
print(temperatura_compressor)
temperatura_compressor.pop(2)
print(temperatura_compressor)
"""

temperaturas = []
for i in range(5):
    temp = int(input(f"Digite a temperatura do compressor {i+1} em °C: "))
    temperaturas.append(temp)


def verificar_alarmes(temperatura):
    if temperatura == "sair":
        return
    if temperatura<70:
        print("Operação normal")
    elif temperatura >= 70 and temperatura < 90:
        print("ATENÇÃO - temperatura elevada")
    elif temperatura >= 90 :
        print("ALARME - temperatura crítica")
    
for i in range(5):
    verificar_alarmes(temperaturas[i])
