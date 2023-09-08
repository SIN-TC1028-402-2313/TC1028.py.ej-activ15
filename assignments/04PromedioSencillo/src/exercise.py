
def main():
    #escribe tu código abajo de esta línea

    t = int(input("Total de numeros a leer:"))

    suma = 0

    for i in range(t):
        n = float(input("Numero:"))

        suma += n
    
    print(f"Promedio={suma/t}")
    
if __name__=='__main__':
    main()