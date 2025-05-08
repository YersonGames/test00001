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

    #Misma escala
    if b == c:
        d = a
    
    print(f"{a} {b}° son {d} {c}°")

def nextl(a,b,c):
    if b == 0:
        return a
    elif b == 1:
        if a == "exit()":
            return 0
        else:
            return c