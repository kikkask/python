def operacao(op, *num):
  total = 0
  if op == "soma":
    for i in num:
      total += i
  elif op == "mult":
    total = 1
    for i in num:
      total *= i
  elif op == "subt":
    for i in num:
      total -= i
  elif op == "divide":
    for i in num:
      total /= i
  else:
    total = "Argumento inválido. Escolha só entre as opções"
  
  return total

opera = input("Digite a operação que vc deseja fazer (soma, mult, subt, divide)")
n = int(input("Quantos números vc quer usar no calculo?"))
list = []
for x in range(n):
  y = int(input("Digite o número"))
  list.append(y)
operacao(opera, list)
