def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """

    gasto = float(input("Ingrese el gasto:"))
    recibido = int(input("Ingrese el recibido:"))
    vuelto = recibido - gasto
    pesos = int(vuelto)
    centavos = int(vuelto*100-(int(vuelto)*100))

    print("Ingresar gasto:")
    print(gasto)
    print("Dinero recibido")
    print(recibido)
    print("")
    print("Vuelto")
    print("")
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)

change()