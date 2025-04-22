import converter
loop1 = True
loop2 = True
loop3 = True

while loop1 == True:
    try:
        tvalue = input("Escribe el valor: ")
        tvalue = float(tvalue)
        loop1 = False
    except ValueError:
        loop1 = True

while loop2 == True:
    try: 
        tscale = input("C - Celsius\nK - Kelvin\nF - Farenheit\nEscribe la escala de la temperatura inicial: ")
        tscale = tscale.upper()
        if tscale == "C" or tscale == "K" or tscale == "F":
            loop2 = False
    except ValueError:
        loop2 = True

while loop3 == True:
    try: 
        tscalef = input("C - Celsius\nK - Kelvin\nF - Farenheit\nEscribe a que escala se convertira: ")
        tscalef = tscalef.upper()
        if tscalef == "C" or tscalef == "K" or tscalef == "F":
            loop3 = False
    except ValueError:
        loop3 = True

converter.convert(tvalue,tscale,tscalef)