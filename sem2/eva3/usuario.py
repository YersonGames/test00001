from database import Database
class Usuario:
    def __init__(self,nombre,contrasenahash,sal):
        self.nombre = nombre
        self.contrasenahash = contrasenahash
        self.sal = sal

    #Getters
    def get_nombre(self):
        return self.nombre

    def get_contrasenahash(self):
        return self.contrasenahash
    
    def get_sal(self):
        return self.sal