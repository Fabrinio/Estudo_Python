class AlunoAcademia:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura
        
    def imc(self):
        return self.peso / (self.altura ** 2)
    
    def pesoMinimo(self):
        return 18.5 * (self.altura ** 2)
    
    def pesoMaximo(self):
        return 24.9 * (self.altura ** 2)
    
    def pesoMedio(self):
        return (self.pesoMinimo() + self.pesoMaximo()) / 2

while True:
    print("1 - Cadastrar novo aluno")
    print("2 - Calcular IMC")
    print("3 - Calcular peso mínimo")
    print("4 - Calcular peso máximo")
    print("5 - Calcular peso médio")
    print("0 - Sair")
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        peso = float(input("Digite o peso do aluno: "))
        altura = float(input("Digite a altura do aluno: "))
        aluno = AlunoAcademia(peso, altura)
        print("Aluno cadastrado com sucesso!")
    elif opcao == 2:
        imc = aluno.imc() if aluno else print("Cadastre um aluno primeiro!")
        print(f"O IMC do aluno é {imc:.2f}")
    elif opcao == 3:
        peso_min = aluno.pesoMinimo() if aluno else print("Cadastre um aluno primeiro!")
        print(f"O peso mínimo do aluno é {peso_min:.2f}")
    elif opcao == 4:
        peso_max = aluno.pesoMaximo() if aluno else print("Cadastre um aluno primeiro!")
        print(f"O peso máximo do aluno é {peso_max:.2f}")
    elif opcao == 5:
        peso_med = aluno.pesoMedio() if aluno else print("Cadastre um aluno primeiro!")
        print(f"O peso médio do aluno é {peso_med:.2f}")
    elif opcao == 0:
        break
    else:
        print("Opção inválida!")
