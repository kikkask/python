# Um programa para receber uma quantidade desconhecida de números e contar quantos estão nos intervalos [0,25],[26,50],[51,75] e [76,100]. A entrada deve terminar quando for lido um número negativo
n = 0
while n >= 0:
  n = int(input("Digite um número"))
  if n >= 0 and n <= 25:
    cont25 += 1
  elif n >= 26 and n <= 50:
    cont50 += 1
  elif n >= 51 and n <= 75:
    cont75 += 1
  elif n >= 76 and n <= 100:
    cont100 += 1
  elif n < 0:
    break
