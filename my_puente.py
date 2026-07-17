import mysql.connector
import time

# 1. Credenciales actualizadas según lo que definimos en el archivo de Docker
credenciales = {
    'host': '127.0.0.1',
    'port': 3307,
    'user': 'root',
    'password': '12345', # La contraseña que pusimos en el YAML
    'database': 'tienda_prueba'
}

print("Esperando a que el contenedor de Docker inicialice el motor...")
time.sleep(5) # Le damos unos segundos al contenedor para arrancar bien la primera vez

try:
    # 2. Conectamos al contenedor de Docker
    conexion = mysql.connector.connect(**credenciales)
    cursor = conexion.cursor()

    # 3. CREACIÓN DE TABLAS (Data Definition Language - DDL)
    # Como tu fuerte es SQL, verás que es el estándar tradicional
    tabla_sql = """
    CREATE TABLE IF NOT EXISTS ventas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        producto VARCHAR(50),
        cantidad INT,
        precio_unitario DECIMAL(10,2)
    )
    """
    cursor.execute(tabla_sql)
    print("Tabla 'ventas' verificada/creada con éxito en el contenedor.")

    # 4. INSERCIÓN DE DATOS (Data Manipulation Language - DML)
    # Primero verificamos si ya hay datos para no duplicarlos cada vez que corras el script
    cursor.execute("SELECT COUNT(*) FROM ventas")
    if cursor.fetchone()[0] == 0:
        insertar_sql = "INSERT INTO ventas (producto, cantidad, precio_unitario) VALUES (%s, %s, %s)"
        datos = [
            ('Laptop', 2, 800.00),
            ('Teclado Mecánico', 5, 50.00),
            ('Monitor 4K', 1, 350.00)
        ]
        cursor.executemany(insertar_sql, datos)
        conexion.commit() # Confirmamos la inserción en el contenedor
        print("Registros iniciales insertados con éxito.")

    # 5. CONSULTA Y EXTRACCIÓN
    cursor.execute("SELECT producto, cantidad, precio_unitario FROM ventas")
    filas = cursor.fetchall()

    print("\n--- DATOS EXTRAÍDOS DESDE EL CONTENEDOR DOCKER ---")
    for fila in filas:
        print(f"Producto: {fila[0]} | Cantidad: {fila[1]} | Precio: ${fila[2]}")

except mysql.connector.Error as error:
    print(f"Error en la infraestructura: {error}")

finally:
    if 'conexion' in locals() and conexion.is_connected():
        cursor.close()
        conexion.close()
        print("\n--- Conexión cerrada limpiamente. ---")