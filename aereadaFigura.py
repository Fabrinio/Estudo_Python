# Escrever um programa que permita ao usuário escolher dentre as 
# figuras geométricas círculo, retângulo e triângulo para calcular a área da figura escolhida. 
# Crie funções para o cálculo de área de cada figura e para um menu de escolha.

def area_circulo(raio):
    ac = 3.14 * (raio ** 2)
    return ac

def area_retangulo(base, altura):
    ar = base * altura
    return ar

def area_triangulo(base, altura):
    at = (base * altura) / 2
    return at

while True:
    print("Escolha uma opção:")
    print("1 - Calcular a área do círculo")
    print("2 - Calcular a área do retângulo")
    print("3 - Calcular a área do triângulo")
    print("0 - Sair")
    opcao = int(input())

    if opcao == 1:
        raio = float(input("Digite o raio: "))
        print(f"A área do círculo é {area_circulo(raio)}")
    elif opcao == 2:
        base = float(input("Digite a base do retângulo: "))
        altura = float(input("Digite a altura do retângulo: "))
        print(f"A área do retângulo é {area_retangulo(base, altura)}")
    elif opcao == 3:
        base = float(input("Digite a base do triângulo: "))
        altura = float(input("Digite a altura do triângulo: "))
        print(f"A área do triângulo é {area_triangulo(base, altura)}")
    elif opcao == 0:
        break
    else:
        print("Opção inválida.")


