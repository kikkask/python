# Calculadora em Python
print("***************** Calculadora em Python *****************")
#Definindo as funções
def add(x,y):
  return x + y
def subtract(x,y):
  return x - y
def multiply(x,y):
  return x * y
def divide(x,y):
  return x / y

# Recebendo os dados
print("Selecione o número da operação desejada:/n")
print("\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão")

opcao = input("Digite sua opção (1/2/3/4): ")
num1 = int(input("\nDigite o primeiro número: "))
num2 = int(input("\nDigite o segundo número: "))

# Chamando as funções e imprimindo o resultado
if opcao == "1":
  print("\n")
  print(num1, " + ", num2, " = ", add(num1,num2))

elif opcao == "2":
  print("\n")
  print(num1, " - ", num2, " = ", subtract(num1,num2))

elif opcao == "3":
  print("\n")
  print(num1, " * ", num2, " = ", multiply(num1,num2))

elif opcao == "4":
  print("\n")
  print(num1, "/", num2, " = ", divide(num1,num2))

else:
  print("\n")
  print('Digite uma opção apenas entre 1 e 4')