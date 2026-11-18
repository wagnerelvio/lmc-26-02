import math

# Sub-rotina 1
def calcular_area(raio):
    return math.pi * raio**2


# Sub-rotina 2
def calcular_circunferencia(raio):
    return 2 * math.pi * raio


# Funcao principal
def main():

    raio = float(input("Digite o raio: "))

    area = calcular_area(raio)

    comprimento = calcular_circunferencia(raio)

    print(f"Area: {area:.2f}")
    print(f"Comprimento: {comprimento:.2f}")


# Executar o programa principal
if __name__ == "__main__":
    main()
