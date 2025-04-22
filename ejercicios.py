def convert(a,b,c):
    #Celsius - Kelvin
    if b == "C" and c == "K":
        d = a+273.15
    if b == "K" and c == "C":
        d = a-273.15
    #Celsius - Fahrenheit
    if b == "C" and c == "F":
        d = (a*(9/5))+32
    if b == "F" and c == "C":
        d = (a*-32)*(5/9)

    #Kelvin - Fahrenheit
    if b == "K" and c == "F":
        d = (a-273.15)*(9/5)+32
    if b == "F" and c == "K":
        d = (a-32)*(5/9)+273.15
    
    print(f"{a} {b}° son {d} {c}°")

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
        if tscale == "C" or tscale == "K" or tscale == "F":
            loop3 = False
    except ValueError:
        loop3 = True

convert(tvalue,tscale,tscalef)