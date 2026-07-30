import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Cargamos el archivo secreto
load_dotenv()

# Jalamos las variables
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

# Armamos la conexión limpia
engine = create_engine(f"mysql+pymysql://root:{password}@{host}:{port}/{database}")

# Ejecutamos la consulta
df = pd.read_sql("SELECT producto, cantidad, precio_unitario FROM ventas", con=engine)
# --- LIMPIEZA DE DATOS ---
# Si hay alguna fila donde no exista nombre de producto, la borramos
df = df.dropna(subset=['producto'])

# Si por error alguien puso cantidad menor a 1, la corregimos a 1
df.loc[df['cantidad'] < 1, 'cantidad'] = 1
    
df['total_venta'] = df['cantidad'] * df['precio_unitario']

# Exportamos a Excel
df.to_excel("reporte_final_ventas.xlsx", index=False)
print("¡Reporte generado de forma segura!") 