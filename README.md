"""
# Gestor de Productos - GraphQL con Python

Este proyecto es un ejemplo sencillo de un **API GraphQL** desarrollado en **Python**
utilizando **Flask** y **Graphene**, sin base de datos (datos quemados en memoria).
Permite consultar todos los productos y buscar uno por su ID.

---

---

## Tecnologías utilizadas

- **Python 3.10+**
- **Flask 2.3.2**
- **Graphene 3.3**
- **Flask-GraphQL 2.0.1**

---

## Cómo ejecutarlo

### 1️Crear entorno virtual
python -m venv venv

### 2️ Activar entorno virtual
- En Windows: venv\Scripts\activate
- En Linux/macOS: source venv/bin/activate

### 3️Instalar dependencias
pip install Flask==2.3.2 graphene==2.1.9 Flask-GraphQL==2.0.1 Werkzeug==2.3.7

### 4️ Ejecutar
python app.py

### 5 Probar en el navegador
http://127.0.0.1:5000/graphql
