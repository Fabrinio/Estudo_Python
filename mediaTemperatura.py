# Definindo as constantes para os nomes dos meses
MESES = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
         'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

# Criando um vetor vazio para armazenar as temperaturas
temperaturas = []

# Loop para solicitar a temperatura de cada mês
for i in range(12):
    temperatura = float(input(f"Digite a temperatura média de {MESES[i]}: "))
    temperaturas.append(temperatura)

# Encontrando a maior e a menor temperatura do ano
maior_temp = max(temperaturas)
menor_temp = min(temperaturas)

# Encontrando os índices (meses) correspondentes à maior e menor temperatura
mes_maior = temperaturas.index(maior_temp)
mes_menor = temperaturas.index(menor_temp)

# Mostrando os resultados
print(f"A maior temperatura do ano foi {maior_temp}°C, em {MESES[mes_maior]}.")
print(f"A menor temperatura do ano foi {menor_temp}°C, em {MESES[mes_menor]}.")
