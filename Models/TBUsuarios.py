from datetime import datetime
import hashlib

class TBUsuarios:
    def __init__(self, data=None):
        if data:
            self.fcusuario_id = data.get('FCUSUARIOID', '')
            self.fcnom_usuario = data.get('FCNOMUSUARIO', '')
            self.fccontrasena = data.get('FCCONTRASENA', '')
            self.fccorreo = data.get('FCCORREO', '')
            self.fccon = data.get('FCCON', '')
            self.fdfec_registro = data.get('FDFECREGISTRO', datetime.now())
            self.fdfec_baja = data.get('FDFECBAJA', datetime.now())
            self.fiestatus = data.get('FIESTATUS', True)
        else:
            self.fcusuario_id = ''
            self.fcnom_usuario = ''
            self.fccontrasena = ''
            self.fccorreo = ''
            self.fccon = ''
            self.fdfec_registro = datetime.now()
            self.fdfec_baja = datetime.now()
            self.fiestatus = True

    def to_dict(self):
        return {
            'FCUSUARIOID': self.fcusuario_id,
            'FCNOMUSUARIO': self.fcnom_usuario,
            'FCCONTRASENA': self.fccontrasena,  # En producción NO devolver contraseña
            'FCCORREO': self.fccorreo,
            'FCCON': self.fccon,
            'FDFECREGISTRO': self.fdfec_registro.isoformat() if isinstance(self.fdfec_registro, datetime) else self.fdfec_registro,
            'FDFECBAJA': self.fdfec_baja.isoformat() if isinstance(self.fdfec_baja, datetime) else self.fdfec_baja,
            'FIESTATUS': self.fiestatus
        }

    def to_dict_safe(self):
        """Versión segura sin contraseña para API"""
        return {
            'FCUSUARIOID': self.fcusuario_id,
            'FCNOMUSUARIO': self.fcnom_usuario,
            'FCCORREO': self.fccorreo,
            'FCCON': self.fccon,
            'FDFECREGISTRO': self.fdfec_registro.isoformat() if isinstance(self.fdfec_registro, datetime) else self.fdfec_registro,
            'FDFECBAJA': self.fdfec_baja.isoformat() if isinstance(self.fdfec_baja, datetime) else self.fdfec_baja,
            'FIESTATUS': self.fiestatus
        }

    def __str__(self):
        return f"TBUsuarios(ID: {self.fcusuario_id}, Usuario: {self.fcnom_usuario}, Email: {self.fccorreo}, Password: {self.fccontrasena}, Status: {self.fiestatus})"

    def __repr__(self):
        return self.__str__()

    # Métodos de validación
    def is_valid(self):
        return (
            self.fcusuario_id and len(self.fcusuario_id) <= 50 and
            self.fcnom_usuario and len(self.fcnom_usuario) <= 50 and
            self.fccorreo and len(self.fccorreo) <= 100 and
            self.fccon and len(self.fccon) <= 150 and
            '@' in self.fccorreo  # Validación básica de email
        )

    # Métodos para manejo de contraseñas
    def hash_password(self, password):
        """Hash de la contraseña usando SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()

    def set_password(self, password):
        """Establece la contraseña hasheada"""
        self.fccontrasena = self.hash_password(password)

    def verify_password(self, password):
        """Verifica si la contraseña es correcta"""
        return self.fccontrasena == self.hash_password(password)

    # Getters y Setters
    def get_usuario_id(self):
        return self.fcusuario_id

    def set_usuario_id(self, usuario_id):
        if len(usuario_id) <= 50:
            self.fcusuario_id = usuario_id
        else:
            raise ValueError("El ID del usuario no puede exceder 50 caracteres")

    def get_nombre_usuario(self):
        return self.fcnom_usuario

    def set_nombre_usuario(self, nombre_usuario):
        if len(nombre_usuario) <= 50:
            self.fcnom_usuario = nombre_usuario
        else:
            raise ValueError("El nombre de usuario no puede exceder 50 caracteres")

    def get_correo(self):
        return self.fccorreo

    def set_correo(self, correo):
        if len(correo) <= 100 and '@' in correo:
            self.fccorreo = correo
        else:
            raise ValueError("El correo no es válido o excede 100 caracteres")

    def get_status(self):
        return self.fiestatus

    def set_status(self, status):
        self.fiestatus = bool(status)

    # Método para crear desde resultado de BD
    @classmethod
    def from_db_row(cls, row):
        return cls({
            'FCUSUARIOID': row.FCUSUARIOID,
            'FCNOMUSUARIO': row.FCNOMUSUARIO,
            'FCCONTRASENA': row.FCCONTRASENA,
            'FCCORREO': row.FCCORREO,
            'FCCON': row.FCCON,
            'FDFECREGISTRO': row.FDFECREGISTRO,
            'FDFECBAJA': row.FDFECBAJA,
            'FIESTATUS': row.FIESTATUS
        })