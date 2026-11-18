# Sub-rotina 1
def calcular_potencia(tensao, corrente):
    return tensao * corrente


# Sub-rotina 2
def calcular_energia(potencia, tempo):
    return (potencia * tempo) / 1000


# Funcao principal
def main():
    tensao = float(input("Tensao em volts: "))
    corrente = float(input("Corrente em amperes: "))
    tempo = float(input("Tempo em horas: "))

    potencia = calcular_potencia(tensao, corrente)
    energia = calcular_energia(potencia, tempo)

    print("Potencia:", potencia, "W")
    print("Energia:", energia, "kWh")


if __name__ == "__main__":
    main()
