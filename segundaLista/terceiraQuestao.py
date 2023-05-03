class Funcionario:
    def __init__(self,matricula, nome, salario):
        self.matricula = matricula
        self.nome = nome
        self.salario = salario

    def ganho_anual(self):
        ganhoAnual = self.salario * 13.0 + (self.salario / 3.0)
        return f"O ganho anual do {self.nome} é de {ganhoAnual:.2f}."
    
    def descontoIR(self):
        if self.salario <= 1500.00:
            return f"O desconto IR do {self.nome} será 0"
        elif self.salario > 1500.00 and self.salario <= 5000.00:
            descontoIR = self.salario * 0.15
            return f"O desconto IR do {self.nome} será {descontoIR:.2f}"
        elif self.salario > 5000.00:
            descontoIR = self.salario * 0.25
            return f"O desconto IR do {self.nome} será {descontoIR:.2f}"
        
while True:
    print("1 - Cadastrar novo funcionário")
    print("2 - Calcular o ganho anual do funcionário")
    print("3 - Calcular o desconto do imposto de renda do funcionário")
    print("0 - Sair")
    opcao = int(input())

    if opcao == 1:
        matricula = str(input("Digite a matrícula do funcionário: "))
        nome = str(input("Digite a nome do funcionário: "))
        salario = float(input("Digite o salario do funcionário: "))
        funcionario = Funcionario(matricula, nome, salario)
        print("Funcionário cadastrado com sucesso")
    elif opcao == 2:
        if not 'funcionario' in locals():
            print("Cadastre um funcionário antes.")
        else:
            ganhoAnual = funcionario.ganho_anual()
            print(ganhoAnual)
    elif opcao == 3:
        if not 'funcionario' in locals():
            print("Cadastre um funcionário antes.")
        else:
            descontoIR = funcionario.descontoIR()
            print(descontoIR)
    elif opcao == 0:
        break
    else:
        print("Opção inválida!")