def eh_divisivel(num1, num2):
    if num1 % num2 == 0:
        print(f"O {num1} é divisível pelo {num2}")
    else:
        print(f"O {num1} não é divisível pelo {num2}")

num1 = float(input("Digite o primeiro número para saber se ele é divisível pelo próximo: "))
num2 = float(input("Digite o segundo número para saber se ele divide o primeiro: "))

eh_divisivel(num1, num2)