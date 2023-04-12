def peso_ideal(altura, sexo):
    if sexo == 'masculino' or sexo == "Masculino":
        p = (72.7 * altura) - 58
        print(f"O seu peso ideal é de {round(p, 2)}")
    elif sexo == 'feminino' or sexo == 'Feminino':
        p = (62.1 * altura) - 44.7
        print(f"O seu peso ideal é de {round(p, 2)}")
    else:
        print("Oops, parece que você digitou errado...")

sexo = str(input("Olá, qual o seu sexo? "))
altura = float(input("E qual é sua altura? "))

peso_ideal(altura, sexo)