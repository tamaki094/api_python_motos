class TBModelos:
    def __init__(self, data=None):
        if data:
            self.fcmodelo_id = data.get('FCMODELOID', '')
            self.fcdescripcion = data.get('FCDESCRIPCION', '')
            self.fiestatus = data.get('FIESTATUS', True)
        else:
            self.fcmodelo_id = ''
            self.fcdescripcion = ''
            self.fiestatus = True

    def to_dict(self):
        return {
            'FCMODELOID': self.fcmodelo_id,
            'FCDESCRIPCION': self.fcdescripcion,
            'FIESTATUS': self.fiestatus
        }

    def __str__(self):
        return f"TBModelos(ID: {self.fcmodelo_id}, Descripción: {self.fcdescripcion}, Status: {self.fiestatus})"

    def __repr__(self):
        return self.__str__()

    # Métodos de validación
    def is_valid(self):
        return (
            self.fcmodelo_id and 
            len(self.fcmodelo_id) <= 50 and
            self.fcdescripcion and 
            len(self.fcdescripcion) <= 100
        )

    # Getters y Setters
    def get_modelo_id(self):
        return self.fcmodelo_id

    def set_modelo_id(self, modelo_id):
        if len(modelo_id) <= 50:
            self.fcmodelo_id = modelo_id
        else:
            raise ValueError("El ID del modelo no puede exceder 50 caracteres")

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