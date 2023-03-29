def numeros():
    x = []

    for i in range(20):
        numero = float(input(f"Informe o {i+1}º numero: "))
        x.append(numero)        
    return sum(x)

print(f"A soma de todos os numeros que vc digitou eh {numeros():.2f}")