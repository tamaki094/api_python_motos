from Data.ItalikaContext import ItalikaContext

from Models.Moto import Moto
from Models.TBCILINDRAJES import TBCILINDRAJES
from Models.TBModelos import TBModelos

class Inventario:

    @staticmethod
    def motosStock(motos : list[Moto]) -> int:
        suma_stock : int = 0

        for moto in motos:
            suma_stock += moto.stock

        return suma_stock
    
    @staticmethod
    def venderMoto(moto : Moto) -> bool:
        ctx : ItalikaContext = ItalikaContext()
        moto : Moto = ctx.getMotoById(moto.moto_id)
        moto.stock -= 1
        ctx.updatetMoto(moto)
        print(moto)

        return True
    
    @staticmethod
    def borrarModelo(moto : Moto) -> bool:
        ctx : ItalikaContext = ItalikaContext()
        moto : Moto = ctx.getMotoById(moto.moto_id)
        ctx.deletetMoto(moto)
        return True
    
    @staticmethod
    def consultarMotos() -> list[Moto]:
        ctx : ItalikaContext = ItalikaContext()
        return ctx.getMotos()
    
    @staticmethod
    def registrarModelo(moto : Moto) -> bool:
        ctx : ItalikaContext = ItalikaContext()
        moto : Moto = ctx.insertMoto(moto)  
        return True
    
    @staticmethod
    def probar_conexion() -> bool:
        ctx: ItalikaContext = ItalikaContext()
        return ctx.conectar()
    
    @staticmethod
    def consultarModelos() -> list[TBModelos]:
        ctx : ItalikaContext = ItalikaContext()
        return ctx.getModelos()
    
    @staticmethod
    def consultarCilindrajes() -> list[TBCILINDRAJES]:
        ctx : ItalikaContext = ItalikaContext()
        return ctx.getCilindrajes()