# Sub-rotina 1
def repeticao_for(n):
    print("Executando o FOR:")

    for i in range(1, n + 1):
        print(i)


# Sub-rotina 2
def repeticao_while(n):
    print("Executando o WHILE:")

    i = 1

    while i <= n:
        print(i)
        i = i + 1


# Funcao principal
def main():
    numero = int(input("Digite um numero: "))

    repeticao_for(numero)
    repeticao_while(numero)


if __name__ == "__main__":
    main()
