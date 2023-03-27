def positivo(num):
    if (num > 0):
        return f"O numero {num} é positivo"
    elif (num < 0):
        return f"O numero {num} é negativo"
    elif (num == 0):
        return f"O numero {num} é zero"


num = float(input("Digite um numero para saber se ele é positivo, negativo ou zero: "))
print(positivo(num))



