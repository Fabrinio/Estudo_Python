# para definir uma função em python se usa def
def bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        return True # ano bissexto
    else:
        return False # não é bissexto

def qtd_bissextos():
    count = 0
    for ano in range(1, 2011):
        if bissexto(ano):
            count += 1
    return count

while True:
    print("Escolha uma opção:")
    print("1 - Verificar se um ano é bissexto")
    print("2 - Calcular quantos anos bissextos ocorreram desde o ano 1 até o ano 2010")
    print("0 - Sair")
    opcao = int(input())

    if opcao == 1:
        ano = int(input("Digite o ano: "))
        if bissexto(ano):
            print(f"{ano} é um ano bissexto.")
        else:
            print(f"{ano} não é um ano bissexto.")
    elif opcao == 2:
        qtd = qtd_bissextos()
        print(f"De 1 até 2010, ocorreram {qtd} anos bissextos.")
    elif opcao == 0:
        break
    else:
        print("Opção inválida.")
