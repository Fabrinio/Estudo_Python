class Hora:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def ehValida(self):
        if self.hora <= 23 and self.minuto <= 59 and self.segundo <= 59:
            return True
        else:
            return False
        
    def imprime(self):
        if self.hora != 0 and self.hora != 1:
            return f"São exatamente => {self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"
        else:
            return f"É => {self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"
    
    def horaDiferenca(self, outra_hora):
        diferenca_segundos = (outra_hora.hora - self.hora) * 3600 + (outra_hora.minuto - self.minuto) * 60 + (outra_hora.segundo - self.segundo)
        horas = diferenca_segundos // 3600
        minutos = (diferenca_segundos % 3600) // 60
        segundos = diferenca_segundos % 60
        return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

    
hora1 = Hora(9, 30, 0)
hora2 = Hora(14, 45, 30)
hora3 = Hora(14, 59, 30)
hora4 = Hora(00, 45, 30)
hora5 = Hora(14, 45, 59)

# utilizando o método horaDiferenca para calcular a diferença entre as duas horas
print(f"A diferença de horas eh de {hora1.horaDiferenca(hora2)}") # retorna (5, 15, 30)
print(f"Está hora eh {hora1.ehValida()}")
# print(f"Está hora eh {hora3.ehValida()}")
# print(f"Está hora eh {hora4.ehValida()}")
# print(f"Está hora eh {hora5.ehValida()}")
print(hora1.imprime())
print(hora2.imprime())
print(hora3.imprime())
print(hora4.imprime())
print(hora5.imprime())

