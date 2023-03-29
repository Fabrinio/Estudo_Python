# Foi realizada uma pesquisa entre quinze habitantes de uma região. 
# Foram coletados estes dados de cada habitante: idade, sexo, salário e 
# número de filhos. Faça uma função que leia esses dados armazenando-os 
# em vetores. Depois, crie funções que recebam esses parâmetros e retornem 
# a média de salário entre os habitantes, a menor e a maior idade do grupo 
# e a quantidade de mulheres com três filhos que recebem até R$ 500,00 (utilize uma função para cada cálculo).

def ler_dados_habitantes():
    idades = []
    sexos = []
    salarios = []
    num_filhos = []

    for i in range(15):
        idade = int(input(f"Informe a idade do {i+1}º habitante: "))
        sexo = input(f"Informe o sexo (M/F) do {i+1}º habitante: ")
        salario = float(input(f"Informe o salário do {i+1}º habitante: "))
        filhos = int(input(f"Informe o número de filhos do {i+1}º habitante: "))
        
        idades.append(idade)
        sexos.append(sexo)
        salarios.append(salario)
        num_filhos.append(filhos)

    return idades, sexos, salarios, num_filhos

def media_salario(salarios):
    return sum(salarios)/len(salarios)

def menor_idade(idades):
    return min(idades)

def maior_idade(idades):
    return max(idades)

def qtde_mulheres_tres_filhos_salario_baixo(sexos, salarios, num_filhos):
    qtde = 0
    for i in range(len(sexos)):
        if sexos[i] == 'F' and num_filhos[i] == 3 and salarios[i] <= 500:
            qtde += 1
    return qtde

idades, sexos, salarios, num_filhos = ler_dados_habitantes()
print("Média de salário dos habitantes:", media_salario(salarios))
print("Menor idade do grupo:", menor_idade(idades))
print("Maior idade do grupo:", maior_idade(idades))
print("Quantidade de mulheres com três filhos e salário até R$ 500,00:",
qtde_mulheres_tres_filhos_salario_baixo(idades, sexos, salarios, num_filhos))