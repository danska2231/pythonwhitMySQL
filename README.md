# Pipeline de Automatización y Análisis de Datos (Docker + MySQL + Pandas)

Este proyecto implementa un flujo completo de ingeniería y análisis de datos en un entorno local moderno y contenerizado.

## 🛠️ Tecnologías Utilizadas
* **Python**: Lógica de integración y automatización.
* **Pandas & SQLAlchemy**: Carga, limpieza y procesamiento analítico de datos en memoria.
* **MySQL 8.0**: Motor de base de datos relacional para almacenamiento transaccional.
* **Docker & Docker Compose**: Contenerización e infraestructura como código para el entorno de desarrollo.
* **Git**: Control de versiones.

## ⚙️ Arquitectura del Proyecto
1. El entorno de base de datos se despliega mediante un contenedor aislado de **Docker** asegurando la portabilidad del sistema.
2. Un script en Python valida la estructura relacional e inyecta datos transaccionales de prueba.
3. Utilizando **SQLAlchemy**, los datos son extraídos mediante consultas dirigidas hacia un DataFrame de **Pandas**.
4. Se ejecutan transformaciones matemáticas sobre el conjunto de datos y se exporta un reporte automatizado en formato Excel de manera limpia.
