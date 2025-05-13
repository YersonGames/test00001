import converter
loop1 = True
loop2 = True
loop3 = True
loop4 = 1
dloop4 = 1
loop5 = True

print("Escribe 'exit()' para salir\n")
while loop5 == True:

    while loop4 == 1:
        while loop4 == 1:
            try:
                tvalue = input("Escribe el valor: ")
                tvalue = float(tvalue)
                loop1 = False
                loop4 = converter.nextl(2,0,loop4)
            except ValueError:
                loop1 = True
                loop4 = converter.nextl(tvalue,1,loop4)

    while loop4 == 2:
        while loop4 == 2:
            try: 
                tscale = input("C - Celsius\nK - Kelvin\nF - Farenheit\nEscribe la escala de la temperatura inicial: ")
                tscale = tscale.upper().strip()
                if tscale == "C" or tscale == "K" or tscale == "F":
                    loop2 = False
                    loop4 = converter.nextl(3,0,loop4)
                else:
                    loop4 = converter.nextl(tscale,1,loop4)
            except ValueError:
                loop2 = True
                loop4 = converter.nextl(tscale,1,loop4)

    while loop4 == 3:
        while loop4 == 3:
            try: 
                tscalef = input("C - Celsius\nK - Kelvin\nF - Farenheit\nEscribe a que escala se convertira: ")
                tscalef = tscalef.upper().strip()
                if tscalef == "C" or tscalef == "K" or tscalef == "F":
                    loop3 = False
                    loop4 = converter.nextl(dloop4,0,loop4)
                    converter.convert(tvalue,tscale,tscalef)
                else:
                    loop4 = converter.nextl(tscalef,1,loop4)
            except ValueError:
                loop3 = True
                loop4 = converter.nextl(tscalef,1,loop4)

    if loop4 == 0:
        exit()