class Moto:
    
    def __init__(self, data=None, modelo=None, precio=None, cilindraje=None, color=None, stock=None, moto_id=None):
        if isinstance(data, dict):
            print("Llamando constructor con diccionario")
            self.moto_id = data.get("moto_id")
            self.modelo = data.get("modelo")
            self.precio = data.get("precio")
            self.cilindraje = data.get("cilindraje")
            self.color = data.get("color")
            self.stock = data.get("stock")
        else:
            print("Llamando constructor con parámetros individuales")
            self.moto_id = moto_id
            self.modelo = modelo
            self.precio = precio
            self.cilindraje = cilindraje
            self.color = color
            self.stock = stock


    

    def __str__(self):
        return f"{self.modelo} ({self.color}) - ${self.precio} | Stock: {self.stock}"
    
    
    def to_dict(self):
        return {
            "moto_id": self.moto_id,
            "modelo": self.modelo,
            "precio": self.precio,
            "cilindraje": self.cilindraje,
            "color": self.color,
            "stock": self.stock
        }
    

