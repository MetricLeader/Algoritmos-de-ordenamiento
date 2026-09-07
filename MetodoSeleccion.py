Numeros = [29, 10, 14, 37, 13]

for Num in range(len(Numeros) -1):
    Menor = Num

    for j in range(Num + 1, len(Numeros)):
        if (Numeros[j] < Numeros[Menor]):
            Menor = j

    if Menor != Num:
        Numeros[Menor], Numeros[Num] = Numeros[Num], Numeros[Menor]

    print(Numeros)

#Juan José Encinas Zuñiga