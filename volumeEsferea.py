def volume_esfera(raio):
    v = (4 / 3) * ( 3.14 * (raio ** 3))
    print(f"O volume da esfera é {v}")

raio = float(input("Digite o volume da esfera: "))
volume_esfera(raio)