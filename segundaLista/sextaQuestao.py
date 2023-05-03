class Funcionario:
    def __init__(self, matricula, nome, salario, ativo):
        self.matricula = matricula
        self.nome = nome
        self.salario = salario
        self.ativo = ativo
    
    def aumenta(self, percentual):
        self.salario = self.salario*percentual + self.salario
        return round(self.salario, 2)
    
    def demite(self):
        if self.ativo is True:
            self.ativo = False
            return "Funcionario demitido"
        else:
            return "O funcionário já está demitido."
        

func1 = Funcionario(1234, "João da Silva", 2500.0, True)
func2 = Funcionario(5678, "Maria Oliveira", 3000.0, False)

print(f"O salario com aumento eh {func1.aumenta(0.1)}")
print(f"O salario com aumento eh { func2.aumenta(0.25)}")

print(func1.demite())
print(func2.demite())