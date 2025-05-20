def operacionfunc(a,b,c):
    if a == 0:
        b+=c
    elif a == 1:
        b-=c
    elif a == 2:
        b /= c
    elif a == 3:
        b *= c
    return b

while(1):
    a = input("Escribe 'exit' para salir\nsuma o resta numeros: ")
    if a == "exit":
        break
    b = 0
    d = 0
    operation = -1
    tempnum = ""
    tempnum2 = ""
    first = 1
    sumaf = 0
    exit_ = 0

    for x in a:
        try:
            c = int(x)
            sumaf = 1
            tempnum += str(c)
            if first == 1:
                b = int(tempnum)
        except ValueError:
            sumaf = 0
            try:
                b = operacionfunc(operation,b,int(tempnum))
            except ValueError:
                print("Error!\n")
                break
            c = x
            first = 0
            tempnum = ""
            if c == "+":
                operation = 0
            elif c == "-":
                operation = 1
            elif c == "/":
                operation = 2
            elif c == "*" or c == "x":
                operation = 3

    if sumaf == 1:
        b = operacionfunc(operation,b,int(tempnum))

    print(f"Resultado: {b}\n")


#if operation == 0:
#            b+=int(tempnum)
#        elif operation == 1:
#            b-=int(tempnum)