def fatorial_de_um_numero(num):
    fatorial = 1
    for i in range(1, num + 1):
        fatorial *= i
    print(f"O resultado do fatorial do número {num} é {fatorial}")

num = int(input("Digite o númeor que vc deseja saber o fatorial: "))
fatorial_de_um_numero(num)