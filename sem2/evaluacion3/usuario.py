class Usuario:
    def __init__(self,nombre,contrasenahash,sal,iteraciones):
        self.nombre = nombre
        self.contrasenahash = contrasenahash
        self.sal = sal
        self.iteraciones = iteraciones

    #Getters
    def get_nombre(self):
        return self.nombre

    def get_contrasenahash(self):
        return self.contrasenahash

    def get_sal(self):
        return self.sal
      
    def get_iteraciones(self):
        return self.iteraciones