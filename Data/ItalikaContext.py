import pyodbc
from Models.TBUsuarios import TBUsuarios
from Models.TBCILINDRAJES import TBCILINDRAJES
from Models.TBModelos import TBModelos
from Models.Moto import Moto

class ItalikaContext:
    conn_str :str

    def __init__(self):
        self.conn_str : str = (           
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=10.81.87.137,1233;"
            "DATABASE=BDItalika;"
            "UID=ITKDentroDeElektra;"
            "PWD=ITKDentroDeElektra11;"
        )


    def conectar(self) -> bool:
        try:
            conn = pyodbc.connect(self.conn_str)
            print("Conexión exitosa a SQL Server.")

            cursor = conn.cursor()
            cursor.execute("select * from dbo.TBMODELOS")
            for row in cursor.fetchall():
                print(row)

            conn.close()
            return True
        except Exception as e:
            print("Error al conectar:", e)
            return False
        
    def getMotos(self) -> list[Moto]:     
        try:
            conn = pyodbc.connect(self.conn_str)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Motos")
            resultados = []

            for row in cursor.fetchall():
                moto = Moto(
                    moto_id= row.MotoID,
                    modelo=row.Modelo,
                    precio=row.Precio,
                    cilindraje=row.Cilindraje,
                    color=row.Color,
                    stock=row.Stock
                )

                resultados.append(moto)
                
            conn.close()
            return resultados           
        except Exception as e:
            print("Error al obtener motos:", e)
            return []
        
    def getMotoById(self, id : int) -> Moto:     
        try:
            conn = pyodbc.connect(self.conn_str)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Motos WHERE MotoID = ?", id)
            moto : Moto

            for row in cursor.fetchall():
                moto = Moto(
                    moto_id= row.MotoID,
                    modelo=row.Modelo,
                    precio=row.Precio,
                    cilindraje=row.Cilindraje,
                    color=row.Color,
                    stock=row.Stock
                )              
                
            conn.close()
            return moto           
        except Exception as e:
            print("Error al obtener motos:", e)
            return Moto()
        
    
    def insertMoto(self, moto: Moto) -> bool:
        try:
            conn = pyodbc.connect(self.conn_str)
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO Motos (Modelo, Precio, Cilindraje, Color, Stock)
                VALUES (?, ?, ?, ?, ?)
            """, moto.modelo, moto.precio, moto.cilindraje, moto.color, moto.stock)

            conn.commit()
            conn.close()
            print("Moto insertada correctamente.")
            return True
        except Exception as e:
            print("Error al insertar moto:", e)
            return False
        

    def updatetMoto(self, moto: Moto) -> bool:
        try:
            conn = pyodbc.connect(self.conn_str)
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE Motos SET Modelo = ?, Precio = ?, Cilindraje = ?, Color = ?, Stock = ?
                WHERE MotoID = ?
            """, moto.modelo, moto.precio, moto.cilindraje, moto.color, moto.stock, moto.moto_id)

            conn.commit()
            conn.close()
            print("Moto actualizada correctamente.")
            return True
        except Exception as e:
            print("Error al actualizar moto:", e)
            return False
        
    def deletetMoto(self, moto: Moto) -> bool:
        try:
            conn = pyodbc.connect(self.conn_str)
            cursor = conn.cursor()

            cursor.execute("""
                DELETE FROM Motos WHERE MotoID = ?
            """, moto.moto_id)

            conn.commit()
            conn.close()
            print("Moto borrada correctamente.")
            return True
        except Exception as e:
            print("Error al borrar moto:", e)
            return False
        
    def getModelos(self) -> list[TBModelos]: # type: ignore
        try:
            conn = pyodbc.connect(self.conn_str)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM dbo.TBMODELOS")
            resultados = []

            for row in cursor.fetchall():
                # Crear diccionario con los datos
                modelo_data = {
                    'FCMODELOID': row.FCMODELOID,
                    'FCDESCRIPCION': row.FCDESCRIPCION,
                    'FIESTATUS': row.FIESTATUS
                }          
                # Pasar el diccionario como parámetro 'data'
                modelo = TBModelos(data=modelo_data)
                resultados.append(modelo)

            conn.close()
            return resultados
        except Exception as e:
            print("Error al obtener modelos:", e)    
            return []
        
    def getModeloById(self, modelo_id: str) -> TBModelos: # type: ignore
        try:
            conn = pyodbc.connect(self.conn_str)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM dbo.TBMODELOS WHERE FCMODELOID = ?", modelo_id)
            row = cursor.fetchone()
            if row:
                modelo_data = {
                    'FCMODELOID': row.FCMODELOID,
                    'FCDESCRIPCION': row.FCDESCRIPCION,
                    'FIESTATUS': row.FIESTATUS
                }
                return TBModelos(data=modelo_data)
            return TBModelos()
        except Exception as e:
            print("Error al obtener modelo por ID:", e)
            return TBModelos()


    def getCilindrajes(self) -> list[TBCILINDRAJES]: # type: ignore
        try:
            conn = pyodbc.connect(self.conn_str)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM dbo.TBCILINDRAJES")
            resultados = []

            for row in cursor.fetchall():
                # Crear diccionario con los datos
                cilindraje_data = {
                    'FICILINDRAJEID': row.FICILINDRAJEID,
                    'FCDESCRIPCION': row.FCDESCRIPCION,
                    'FIESTATUS': row.FIESTATUS
                }          
                # Pasar el diccionario como parámetro 'data'
                cilindraje = TBCILINDRAJES(data=cilindraje_data)
                resultados.append(cilindraje)

            conn.close()
            return resultados
        except Exception as e:
            print("Error al obtener cilindrajes:", e)    
            return []
        
    def getUserByUserName(self, username: str) -> TBUsuarios: # type: ignore
        try:
            conn = pyodbc.connect(self.conn_str)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM dbo.TBUSUARIOS WHERE FCNOMUSUARIO = ?", username)
            row = cursor.fetchone()
            if row:
                return TBUsuarios.from_db_row(row)
            return TBUsuarios()
        except Exception as e:
            print("Error al obtener usuario por nombre:", e)
            return TBUsuarios()
