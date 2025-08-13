list_notas = [["Jose",[7.0,4.5,5.6]],["Maria",[6.1,6.4,3.6]]]

for x in list_notas:
    suma = 0
    for i in range(len(x[1])):
        print(f"{x[0]}: {x[1][i]}")
        suma += x[1][i]
    print(f"promedio: {suma/len(x[1])}")