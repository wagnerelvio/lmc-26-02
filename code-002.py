# Sub-rotina 1
def calcular_area(base, altura):
    return base * altura


# Sub-rotina 2
def calcular_perimetro(base, altura):
    return 2 * (base + altura)


# Funcao principal
def main():
    base = float(input("Digite a base: "))
    altura = float(input("Digite a altura: "))

    area = calcular_area(base, altura)
    perimetro = calcular_perimetro(base, altura)

    print("Area:", area)
    print("Perimetro:", perimetro)


if __name__ == "__main__":
    main()
