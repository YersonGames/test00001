list_movie = ["Destino final","Eternauta","Lilo y stich","Los priratas del carible"]
num = 1
print("Con for:")
for x in list_movie:
    print(f"pelicula {num}: {x}")
    num +=1


print("\nCon while:")
count = 0

while count < len(list_movie):
    print(f"Pelicula {count+1}: {list_movie[count]}")
    count += 1

print("")

for i in range(0,len(list_movie)):
    print(f"Pelicula {i+1}: {list_movie[i]}")
print(list_movie[2])a