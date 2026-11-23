frase = input("Digite uma frase: ")
vogais = "aeiou"
total_vogais = 0

for letra in frase:
  if letra in vogais:
    total_vogais += 1

print("A frase possui ",total_vogais," vogais")