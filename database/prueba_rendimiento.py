import os
import time
from dotenv import load_dotenv
import mysql.connector

# Cargamos el archivo secreto
load_dotenv()

# Jalamos las variables
conexion = mysql.connector.connect(
host = os.getenv("DB_HOST"),
port = os.getenv("DB_PORT"),
user = "root",
password = os.getenv("DB_PASSWORD"),
database = os.getenv("DB_NAME")
)
cursor = conexion.cursor()

# 1. Consulta SIN ÍNDICE (Full Table Scan)
print("1. Buscando registros de 'Silla Ergonómica' SIN ÍNDICE...")
inicio = time.time()
cursor.execute("SELECT COUNT(*), SUM(cantidad * precio_unitario) FROM ventas WHERE producto = 'Silla Ergonómica'")
resultado = cursor.fetchone()
fin = time.time()
tiempo_sin_indice = fin - inicio
print(f"Resultado: Total Ventas = ${resultado[1]:,.2f}")
print(f"Tiempo SIN índice: {tiempo_sin_indice:.4f} segundos")

# 2. Creamos un ÍNDICE B-Tree en la columna 'producto'
print("\n2. Creando índice B-Tree en la columna 'producto'...")
try:
    cursor.execute("CREATE INDEX idx_producto ON ventas(|)")
    conexion.commit()
    print("   ¡Índice 'idx_producto' creado exitosamente!")
except mysql.connector.Error as err:
    print("   El índice ya existía o no se pudo crear.")

# 3. Consulta CON ÍNDICE
print("\n3. Repitiendo la búsqueda CON ÍNDICE B-Tree...")
inicio = time.time()
cursor.execute("SELECT COUNT(*), SUM(cantidad * precio_unitario) FROM ventas WHERE producto = 'Silla Ergonómica'")
resultado = cursor.fetchone()
fin = time.time()
tiempo_con_indice = fin - inicio
print(f"   Resultado: Total Ventas = ${resultado[1]:,.2f}")
print(f"   ⏱️ Tiempo CON índice: {tiempo_con_indice:.4f} segundos")

mejora = (tiempo_sin_indice - tiempo_con_indice) / tiempo_sin_indice * 100
print(f"\n🚀 ¡Mejora de rendimiento: {mejora:.2f}% más rápido!")


print ("\n4.Haciendo Consulta de la tabla")
cursor.execute("SELECT * FROM ventas")
resultado = cursor.fetchone()

while resultado is not None:
    print (resultado)
    resultado = cursor.fetchone()

cursor.close()
conexion.close()