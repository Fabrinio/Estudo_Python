def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def primos_acima_de_100():
    primos = []
    n =     1
    while len(primos) < 10:
        if eh_primo(n):
            primos.append(n)
        n += 1
    print(primos)

primos_acima_de_100()
