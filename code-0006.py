# Sub-rotina 1
def calcular_media(t1, t2, t3):
    return (t1 + t2 + t3) / 3


# Sub-rotina 2
def verificar_temperatura(media):
    if media > 30:
        print("Alerta: temperatura elevada")
    else:
        print("Temperatura normal")


# Funcao principal
def main():
    t1 = float(input("Temperatura do sensor 1: "))
    t2 = float(input("Temperatura do sensor 2: "))
    t3 = float(input("Temperatura do sensor 3: "))

    media = calcular_media(t1, t2, t3)

    print("Temperatura media:", media)

    verificar_temperatura(media)


if __name__ == "__main__":
    main()
