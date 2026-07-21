from sqlalchemy import create_engine
import pandas as pd

class MySQLRepository:
    def __init__(self, connection_string: str):
        # El motor se crea una sola vez al instanciar la clase
        self.engine = create_engine(connection_string)
        
    def obtener_datos(self, query: str) -> pd.DataFrame:
        """Extrae cualquier consulta y la devuelve como un DataFrame limpio"""
        try:
            return pd.read_sql(query, con=self.engine)
        except Exception as e:
            raise RuntimeError(f"Error crítico al consultar la base de datos: {e}")