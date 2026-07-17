import pandas as pd
from sqlalchemy import create_engine

# 1. Creamos la conexión al contenedor de Docker usando SQLAlchemy
# Formato: mysql+pymysql://usuario:password@host:puerto/base_de_datos
# Usa el puerto 3307 si cambiaste el puerto en tu docker-compose, o 3306 si liberaste el puerto.
engine = create_engine("mysql+pymysql://root:12345@127.0.0.1:3307/tienda_prueba")

try:
    # 2. Tu fuerte: la consulta SQL
    query = "SELECT producto, cantidad, precio_unitario FROM ventas"

    # 3. ¡La magia de Pandas! Lee directamente desde el motor de base de datos
    df = pd.read_sql(query, con=engine)

    print("--- 1. DATOS CARGADOS EN UN DATAFRAME DE PANDAS ---")
    print(df)
    print("\n---------------------------------------------------")

    # 4. CIENCIA DE DATOS / PROCESAMIENTO RÁPIDO
    # Creamos una columna calculada al vuelo multiplicando dos columnas existentes
    df['total_venta'] = df['cantidad'] * df['precio_unitario']

    print("--- 2. DATAFRAME CON NUEVA COLUMNA DE TOTALES ---")
    print(df)
    print("\n---------------------------------------------------")

    # 5. EXPORTACIÓN AUTOMÁTICA
    # Guardamos el resultado procesado en un archivo Excel real en tu carpeta
    df.to_excel("reporte_final_ventas.xlsx", index=False)
    print("¡Reporte 'reporte_final_ventas.xlsx' generado con éxito!")

except Exception as e:
    print(f"Ocurrió un error en el análisis: {e}")