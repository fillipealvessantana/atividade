texto = input("Digite uma palavra ou frase: ")
limpo = texto.replace(" ", "")

if limpo == limpo[::-1]:
  print("É um palíndromo!")
else:
  print("Não é um palíndromo.")