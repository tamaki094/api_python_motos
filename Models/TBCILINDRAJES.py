class TBCILINDRAJES:
    def __init__(self, data=None):
        if data:
            self.ficilindrajeid = data.get('FICILINDRAJEID', 0)
            self.fcdescripcion = data.get('FCDESCRIPCION', '')
            self.fiestatus = data.get('FIESTATUS', True)
        else:
            self.ficilindrajeid = 0
            self.fcdescripcion = ''
            self.fiestatus = True

    def to_dict(self):
        return {
            'FICILINDRAJEID': self.ficilindrajeid,
            'FCDESCRIPCION': self.fcdescripcion,
            'FIESTATUS': self.fiestatus
        }

    def __str__(self):
        return f"TBCILINDRAJES(ID: {self.ficilindrajeid}, Descripción: {self.fcdescripcion}, Status: {self.fiestatus})"

    def __repr__(self):
        return self.__str__()

    # Métodos de validación
    def is_valid(self):
        return (
            self.ficilindrajeid > 0 and
            self.fcdescripcion and 
            len(self.fcdescripcion) <= 100
        )

    # Getters y Setters
    def get_cilindraje_id(self):
        return self.ficilindrajeid

    def set_cilindraje_id(self, cilindraje_id):
        if isinstance(cilindraje_id, int) and cilindraje_id > 0:
            self.ficilindrajeid = cilindraje_id
        else:
            raise ValueError("El ID del cilindraje debe ser un entero positivo")

    def get_descripcion(self):
        return self.fcdescripcion

    def set_descripcion(self, descripcion):
        if len(descripcion) <= 100:
            self.fcdescripcion = descripcion
        else:
            raise ValueError("La descripción no puede exceder 100 caracteres")

    def get_status(self):
        return self.fiestatus

    def set_status(self, status):
        self.fiestatus = bool(status)

    # Método para crear desde resultado de BD
    @classmethod
    def from_db_row(cls, row):
        return cls({
            'FICILINDRAJEID': row.FICILINDRAJEID,
            'FCDESCRIPCION': row.FCDESCRIPCION,
            'FIESTATUS': row.FIESTATUS
        })