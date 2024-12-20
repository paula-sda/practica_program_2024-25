#!/bin/bash

# Verificar si el entorno virtual ya existe
if [ -d ".env" ]; then
    echo "Eliminando el entorno virtual existente..."
    rm -rf .env
fi

# Crear el entorno virtual nuevamente
echo "Creando un nuevo entorno virtual..."
python3 -m venv .env

# Activar el entorno virtual
echo "Activando el entorno virtual..."
source .env/bin/activate

cd src

# Instalar dependencias del archivo requirements.txt
echo "Instalando dependencias..."
pip install -r requirements.txt

# Ejecutar el archivo main.py
echo "Lanzando main.py..."
python3 -u MAIN.py

# Desactivar el entorno virtual al finalizar
deactivate

