def numeros():
    x = []

    for i in range(15):
        numero = int(input(f"Informe o {i+1}º numero: "))
        x.append(numero)        
    return x

def num_par(x):
    qtd = 0
    for i in range(len(x)):
        if x[i] % 2 == 0:
            qtd += 1
    return qtd    


print(f"A quantidade de numeros pares eh de {num_par(numeros())}")
