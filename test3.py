import math
b = 0
loop1 = True
a = input("aaa: ").split("+")
while loop1 == True:
    for x in a:
        try:
            b = b+int(x)
            loop1 = False
        except ValueError:
            loop1 = True
            b=0
            a = input("aaa: ").split("+")
print(b)