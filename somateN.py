def soma_ate_n(n):
    if (n > 0 ):
        soma = 0 
        for i in range(n+1):
            soma += i
        print(f"A soma dos números é {soma}")
    else:
        print(f"O número {n} não é inteiro ou positivo")
    
n = int(input("Digite um número para somar todos os números antes dele e ele mesmo: "))
soma_ate_n(n)

