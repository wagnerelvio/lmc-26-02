# Sub-rotina 1
def calcular_media(n1, n2):
    return (n1 + n2) / 2


# Sub-rotina 2
def verificar_situacao(media):
    if media >= 7:
        print("Aluno aprovado")
    else:
        print("Aluno reprovado")


# Funcao principal
def main():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = calcular_media(nota1, nota2)

    print("Media:", media)

    verificar_situacao(media)


if __name__ == "__main__":
    main()
