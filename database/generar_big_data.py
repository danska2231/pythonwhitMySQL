import os
import time
import random
from dotenv import load_dotenv
import mysql.connector
from faker import Faker

# Cargamos el archivo secreto
load_dotenv()

# Jalamos las variables
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

# Inicializamos el generador de datos falsos
fake = Faker('es_ES')

# Productos disponibles para variar
PRODUCTOS = ['Laptop', 'Teclado Mecánico', 'Monitor 4K', 'Mouse Inalámbrico', 'Audífonos Gamer', 'Silla Ergonómica', 'Escritorio Elevable']

def generar_millon_registros():
    print(f"Conectando a MySQL en {host}:{port}...")
    
    conexion = mysql.connector.connect(
        host=host,
        port=port,
        user='root',
        password=password,
        database=database
    )
    cursor = conexion.cursor()

    # Desactivamos temporalmente los autocommits para máxima velocidad
    conexion.autocommit = False

    print("\n--- INICIANDO GENERACIÓN DE 1,000,000 DE REGISTROS ---")
    tiempo_inicio = time.time()

    TOTAL_REGISTROS = 1_000_000
    TAMAÑO_LOTE = 50_000  # Insertamos en bloques de 50,000
    
    insert_query = """
        INSERT INTO ventas (producto, cantidad, precio_unitario) 
        VALUES (%s, %s, %s)
    """

    registros_insertados = 0

    while registros_insertados < TOTAL_REGISTROS:
        lote = []
        for _ in range(TAMAÑO_LOTE):
            producto = random.choice(PRODUCTOS)
            cantidad = random.randint(1, 10)
            precio = round(random.uniform(15.0, 1200.0), 2)
            lote.append((producto, cantidad, precio))

        # Inserción masiva en bloque
        cursor.executemany(insert_query, lote)
        conexion.commit() # Confirmamos el paquete completo
        
        registros_insertados += TAMAÑO_LOTE
        print(f"Procesados: {registros_insertados:,} / {TOTAL_REGISTROS:,} filas...")

    tiempo_total = time.time() - tiempo_inicio
    print(f"\n¡ÉXITO TOTAL! 1,000,000 de registros insertados en {tiempo_total:.2f} segundos.")

    cursor.close()
    conexion.close()

if __name__ == "__main__":
    generar_millon_registros()