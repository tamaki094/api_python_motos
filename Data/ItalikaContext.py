import pyodbc
from Models.Moto import Moto

class ItalikaContext:
    conn_str :str

    def __init__(self):
        self.conn_str : str = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost\\SQLEXPRESS;"
            "DATABASE=ITALIKA;"
            "Trusted_Connection=yes;"
        )


    def conectar(self) -> bool:
        try:
            conn = pyodbc.connect(self.conn_str)
            print("Conexión exitosa a SQL Server.")

            cursor = conn.cursor()
            cursor.execute("SELECT TOP 5 * FROM Motos")
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



