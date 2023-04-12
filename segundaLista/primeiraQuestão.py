class Numero:
    def __init__(self, n):
        self.n = n

    def fatorial(self):
        fatorial = 1.0
        i = 1.0
        while i <= self.n:
            fatorial *= i
            i += 1.0
        return (f"O resultado do fatorial do número {self.n} é {fatorial}")
    
    def potencia(self, x):
        res = self.n ** x
        return (f"O resultado da potencia de base {self.n} e expoente {x} é de {round(res, 2)}")
    
    def parte_inteira(self):
        return (f"A parte inteira de {self.n} é {int(self.n)}")

    def parte_decimal(self):
        return (f"A parte decimal de {self.n} é {round(self.n - int(self.n), 2)}")
    
while True:
    print("1 - Entrar no sistema")
    print("0 - Sair do Sistema")
    opcao = int(input())

    if opcao == 1:
        while True:
            print("1 - Calcular fatorial")
            print("2 - Calcular potencia")
            print("3 - Calcular a parte inteira")
            print("4 - Calcular a parte decimal")
            print("0 - Voltar para Menu Inicial")

            op = int(input())

            if op == 1:
                n = float(input("Digite o número que você deseja: "))
                num = Numero(n)

                print(num.fatorial())
            elif op == 2:
                n = float(input("Digite o número que você deseja: "))
                num = Numero(n)

                x = int(input("Digite o número que servirá como expoente: "))

                print(num.potencia(x))
            elif op == 3:
                n = float(input("Digite o número que você deseja: "))
                num = Numero(n)

                print(num.parte_inteira())
            elif op == 4:
                n = float(input("Digite o número que você deseja: "))
                num = Numero(n)

                print(num.parte_decimal())
            elif op == 0:
                break
            else:
                print("Comando não existe")
    elif op == 0:
        break
    else:
        print("Comando não existe")
                
            





