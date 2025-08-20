class Auto:
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    #Getters
    def get_marca(self):
        return self.marca
    def get_modelo(self):
        return self.modelo
    def get_ano(self):
        return self.ano

    #Setters
    def set_marca(self,new_marca):
        self.marca = new_marca
    def set_modelo(self,new_modelo):
        self.modelo = new_modelo
    def set_ano(self,new_ano):
        self.ano = new_ano

    def display_info(self):
        print(f"Marca: {self.get_marca()}\nModelo: {self.get_modelo()}\nAño: {self.get_ano()}")

miauto = Auto("Toyota","aaaa",1212)

miauto.display_info()