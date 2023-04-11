def eh_tri(num1, num2, num3):
    if num1 <= num2 + num3 and num2 <= num1 + num3 and num3 <= num1 + num2:
        return True
    else:
        return False
    
def tipo_tri():
    if eh_tri(num1, num2, num3):
        if num1 != num2 and num1 != num3 and num2 != num3:
            print("O triângulo é do tipo escaleno.")
        elif (num1 == num2 and num2 != num3) or (num2 == num3 and num3 != num1) or (num1 == num3 and num3 != num2):
            print("O triângulo é do tipo isóseles.")
        elif num1 == num2 and num2 == num3:
            print("O triângulo é do tipo equilátero.")
    else:
     print("Não é um triângulo.")

while True:

    print("1 - Verificar o triângulo")
    print("0 - Sair")
    opcao = int(input())

    if opcao == 1:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        num3 = float(input("Digite o terceiro número: "))
        tipo_tri()
    elif opcao == 0:
        break
    else:
        print("Opção inválida!")