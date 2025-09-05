class Persona:
    def __init__(self,rut,nombre):
        self.rut = rut
        self.nombre = nombre

    def presentarse(self):
        return f"Soy {self.nombre}\nRut: {self.rut}"
    
class Estudiante(Persona):
    def __init__(self, rut, nombre,carrera):
        super().__init__(rut, nombre)
        self.carrera = carrera
    
    def presentarse(self):
        base = super().presentarse()
        return f"{base}\nCarrera: {self.carrera}"

class Docente(Persona):
    def __init__(self, rut, nombre,asignatura):
        super().__init__(rut, nombre)
        self.asignatura = asignatura
    
    def presentarse(self):
        base = super().presentarse()
        return f"{base}\nAsignatura: {self.asignatura}"
    
a = Estudiante("22198823-k","Yerson","Ingenieria informatica")
a2 = Docente("12854678-1","Javier","Ingenieria informatica")
a3 = Persona("12345678-1","Jose")

print(a.presentarse())
print(a2.presentarse())
print(a3.presentarse())
a