#Functions
def suma(a,b):
    result = a+b
    print(f"el resultado de la suma es: {result}")

def resta(a,b):
    result = a-b
    print(f"el resultado de la resta es: {result}")

def mult(a,b):
    result = a*b
    print(f"el resultado de la multiplicacion es: {result}")

def divi(a,b):
    result = a/b
    print(f"el resultado de la division es: {result}")

loop3 = False
_exit = "5"

print(f"1) Suma\n2) Resta\n3) Multiplicacion\n4) Division\n{_exit}) Salir")

while loop3 == False:
    select = input("Ingrese una opcion: ")

    if select == _exit:
        loop3 = True
        break


    #Variables
    a = ""
    b = ""
    cont = False
    loop1 = False
    loop2 = False

    while cont == False:
        if select.isdigit() == False:
            select = input("Ingrese una opcion: ")
        else:
            select = int(select)
            if select == 1 or select == 2 or select == 3 or select == 4:
                cont = True
            else:
                select = ""

    #Primer numero
    while loop1 == False:
        try:
            a = input("Ingrese el primer numero: ")
            a = float(a)
            loop1 = True
        except ValueError:
            loop1 = False

    #Segundo numero
    while loop2 == False:
        if select != 4: #Suma, resta, multiplicacion
            try:
                b = input("Ingrese el segundo numero: ")
                b = float(b)
                loop2 = True
            except ValueError:
                loop2 = False
        else: #Si es division
            try:
                b = input("Ingrese el segundo numero: ")
                b = float(b)
                if b == 0:
                    print("No se puede dividir por 0")
                else:
                    loop2 = True
            except ValueError:
                loop2 = False
            
    #Calcular
    if select == 1:
        suma(a,b)
    elif select == 2:
        resta(a,b)
    elif select == 3:
        mult(a,b)
    elif select == 4:
        divi(a,b)
    print()