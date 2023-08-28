'''def mult(a,b):
    return a * b


v1 = int(input("digite o primeiro valor: "))
v2 = int(input("digite o segundo valor: "))

resultado = mult(v1, v2)

print(resultado)'''

def imc(peso,altura):
    return(peso / altura ** 2)

peso = float(input("digite seu peso: "))
altura = float(input("digite sua altura: "))

resultado = imc(peso,altura)
print(resultado)

if resultado < 18.5:
    print("abaixo do peso")
elif resultado <= 24.9:
    print("peso normal")
elif resultado <=29.9:
    print("excesso de peso")
elif resultado < 35:
    print("obesidade")
else:
print("obesidade extrema")