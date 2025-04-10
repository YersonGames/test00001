#While
count = 0

while count != 100:
    count += 1
    print(count)

#For
numbers = [10,20,30,40]
dictionary = {"nombre":"Yerson","apellido":"Cheuquehuala","edad":"18"}

blocks = ["Cobblestone","Dirt","Grass","Andesite"]

for Block in blocks:
    print(Block)

for number in numbers:
    result = number * number
    print(f"Hola {number} * {number} = {result}")
    
for x in dictionary.items():
    key = x[0]
    value = x[1]
    print(f"Key: {key}. Value: {value}")
    

#Functions
def test01(nombre):
    print(f"hola {nombre}")
    
test01("maria")