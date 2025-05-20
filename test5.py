a = input("suma o resta numeros: ")
b = 0
d = 0
operation = -1
tempnum = ""
tempnum2 = ""
first = 1
sumaf = 0

for x in a:
    try:
        c = int(x)
        sumaf = 1
        tempnum += str(c)
        if first == 1:
            b = int(tempnum)
    except ValueError:
        sumaf = 0
        if operation == 0:
            b+=int(tempnum)
        elif operation == 1:
            b-=int(tempnum)
        c = x
        first = 0
        tempnum = ""
        if c == "+":
            operation = 0
        elif c == "-":
            operation = 1

if sumaf == 1:
    if operation == 0:
        b+=int(tempnum)
    elif operation == 1:
        b-=int(tempnum)

print(f"resultado: {b}")