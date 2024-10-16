n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
soma = n1 + n2
if soma >= 0:
  print("A soma de {} e {} é igual a {} , logo o número é positivo".format(n1,n2,soma))
else:
  print("A soma de {} e {} é igual a {}, logo o número é negativo".format(n1,n2,soma))