class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        

    def mostrar_info(self):
        print(f"{self.marca} {self.modelo} ")

    def encender(self):
        print(f"{self.marca} {self.modelo} esta encendido.")

#Clase hija
class Auto(Vehiculo):
    def __init__(self, marca, modelo, anio):
        super().__init__(marca, modelo) #llamar al constructor del padre
        self.anio = anio

    def mostrar_info(self): #sobrecarga
        print(f"{self.marca} {self.modelo} {self.anio}")

    def encender(self):
        print(f"{self.marca} {self.modelo} ruge al encenderse.")

class Moto(Vehiculo):
    def encender(self):
        print(f"{self.marca} {self.modelo} arranca con rugido fuerte.")

#programa principal 
# vehiculo = Vehiculo("Suzuki", "Vitara")
# vehiculo.mostrar_info()
# vehiculo.encender()

# auto = Auto("BMW","M3", 2010)
# auto.mostrar_info()
# auto.encender()
        
# moto = Moto("Yamaha", "R6")
# moto.mostrar_info()
# moto.encender()

vehiculos = [Vehiculo("Suzuki", "Vitara"),
            Auto("BMW","M3", 2010),
            Moto("Yamaha","R6")]

for v in vehiculos:
    v.encender()
