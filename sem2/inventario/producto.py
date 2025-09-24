class Producto:
    def __init__(self,id: str,nombre: str,precio: float,stock: int):
        self.id = None
        self.nombre = None
        self.precio = None
        self.stock = None
        
        self.set_id(id)
        self.set_nombre(nombre)
        self.set_precio(precio)
        self.set_stock(stock)
        
    #Getters
    def get_id(self):
        return self.id
    def get_nombre(self):
        return self.nombre
    def get_precio(self):
        return self.precio
    def get_stock(self):
        return self.stock
    
    #Setters
    def set_id(self, new_id: str):
        if len(new_id) != 0 and not new_id.strip():
            raise ValueError ("El codigo no puede estar vacio")
        self.id = new_id
    
    def set_nombre(self, new_nombre: str):
        if len(new_nombre) != 0 and not new_nombre.strip():
            raise ValueError ("El nombre no puede estar vacio")
        self.nombre = new_nombre
        
    def set_precio(self, new_precio: float):
        try:
            precio = float(new_precio)
            if precio <= 0:
                raise ValueError("El precio debe ser mayor a cero")
            else:
                self.precio = precio
        except ValueError:
            print("El precio debe ser un numero")
            
    def set_stock(self, new_stock: int):
        try:
            stock = int(new_stock)
            if stock <= 0:
                raise ValueError("El stock debe ser mayor a cero")
            else:
                self.stock = stock
        except :
            raise ValueError("El stock debe ser un numero")
            
    def mostrar_info(self):
        precio_fmt = f"{self.precio:,.0f}".replace(",",".")
        return f"[{self.id}] {self.nombre} - ${precio_fmt} {self.stock}"