def potencia(x,a):
    resultado = 1
    for i in range (a):
        resultado *= x 
    return resultado

x = int(input("Digite a base da potência: "))
a = int(input("Digite o expoente da potência: "))

print(f"O resultado da pontencia de base {x} e expoente {a} eh de {potencia(x,a)}")