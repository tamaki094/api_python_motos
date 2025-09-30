from Data.ItalikaContext import ItalikaContext
from Models.TBUsuarios import TBUsuarios

class Accesos:
    @staticmethod
    def validate_user(username: str, password: str) -> bool:
        ctx : ItalikaContext = ItalikaContext()
        user : TBUsuarios = ctx.getUserByUserName(username)
        print("Usuario obtenido:", user)
        if user and user.fccontrasena == password:
            return True
        return False
