def media_valores():
    valores = []
    while True:
        valor = float(input("Digite um valor positivo (ou um número negativo para sair): "))
        if valor < 0:
            break
        valores.append(valor)
    if len(valores) == 0:
        return 0
    media = sum(valores) / len(valores)
    return media

print(f"A média dos valores digitados é {media_valores()}")