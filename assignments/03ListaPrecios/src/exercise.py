def getPrecio(clave):
    if  clave== "A":
        return 120
    elif clave == "B":
        return 250
    elif clave == "C":
        return 360
    else:
        return 0

def main():
    #escribe tu código abajo de esta línea

    clave=""
    suma=0

    while clave != "X":
        clave = input("Clave:")

        precio = getPrecio(clave)

        if precio != 0:
            print(f"Precio={precio}")
            
        suma += precio

    print(f"Total de la compra: {suma}")
    
if __name__=='__main__':
    main()