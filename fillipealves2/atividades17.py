import random

secreto = random.randint(1, 100)
tentativas = 0

while True:
  try:
    palpite = int(input("Adivinhe o número (1 a 100): "))
    tentativas += 1

    if palpite < secreto:
      print("Mais alto!")
    elif palpite > secreto:
      print("Mais baixo!")
    else:
      print("Parabéns! Você acertou em" ,tentativas, "tentativas.")
      break
  except ValueError:
    print("Entrada inválida! Digite apenas números inteiros.")