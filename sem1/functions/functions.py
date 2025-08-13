#Functions
def test01(nombre):
    print(f"hola {nombre}")

def suma(x,y):
    result = x+y
    print(f"El resultado de la suma es {result}")

name = input()  
test01(name)

number1 = 0
number2 = 0

number1 = input("El primero numero: ")

while (number1.isdigit() == False):
    number1 = input("El primero numero: ")
number1 = int(number1)

number2 = input("El segundo numero: ")

while (number2.isdigit() == False):
    number2 = input("El segundo numero: ")
number2 = int(number2)

suma(number1,number2)