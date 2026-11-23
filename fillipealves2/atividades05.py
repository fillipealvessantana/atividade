valor = float(input("Digite e preço do produto: "))
if valor > 100:
    pagar = valor * 0.90
    print("Parabens voce ganhou 10% de desconto e vai pagar", pagar, "reais")
else:
    print("não tem desconto, o valor é",valor)