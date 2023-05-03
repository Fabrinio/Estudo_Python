class Onibus:
    def __init__(self, max_passageiros, preco_passagem, faturamento_total, passageiros_in):
        self.max_passageiros = max_passageiros
        self.preco_passagem = preco_passagem
        self.faturamento_total = faturamento_total
        self.passageiros_in = passageiros_in
        

    def entrar(self, qtdPassageiros):
        if qtdPassageiros + self.passageiros_in > self.max_passageiros:
            return False
        else:
            self.passageiros_in += qtdPassageiros
            self.faturamento_total += qtdPassageiros * self.preco_passagem
            return True
    def sair(self, qtdPassageiros):
        if qtdPassageiros > self.passageiros_in:
            return False
        else:
            self.passageiros_in -= qtdPassageiros
            return True
        
    def faturamento(self):
        return self.faturamento_total

    def passageiros_in_bus(self):
        return self.passageiros_in
    

onibus = Onibus(50, 5.0, 0.0, 0)

print("Quantidade de passageiros no ônibus:", onibus.passageiros_in_bus())
print("Faturamento total:", onibus.faturamento())

if onibus.entrar(30):
    print("30 passageiros entraram no ônibus.")
else:
    print("Não há espaço suficiente para 30 passageiros.")

print("Quantidade de passageiros no ônibus:", onibus.passageiros_in_bus())
print("Faturamento total:", onibus.faturamento())

if onibus.sair(10):
    print("10 passageiros saíram do ônibus.")
else:
    print("Não há passageiros suficientes para sair.")

print("Quantidade de passageiros no ônibus:", onibus.passageiros_in_bus())
print("Faturamento total:", onibus.faturamento())

if onibus.entrar(5):
    print(f"x passageiros entraram no ônibus.")
else:
    print("Não há espaço suficiente para x passageiros.")

print("Quantidade de passageiros no ônibus:", onibus.passageiros_in_bus())
print("Faturamento total:", onibus.faturamento())

if onibus.sair(26):
    print("10 passageiros saíram do ônibus.")
else:
    print("Não há passageiros suficientes para sair.")

print("Quantidade de passageiros no ônibus:", onibus.passageiros_in_bus())
print("Faturamento total:", onibus.faturamento())

