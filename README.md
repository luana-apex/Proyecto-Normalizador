# Normalizador de Números Telefónicos Argentinos

Este programa permite normalizar números telefónicos argentinos a un formato estándar.

## Requisitos

- Python 3.x
- pandas

## Instalación

1. Asegúrate de tener Python 3.x instalado.
2. Instala las dependencias:
   ```
   pip install pandas
   ```

## Uso

1. Coloca el archivo `arg_phone_standardizer.py` en una carpeta.
2. Asegúrate de que la carpeta `area_codes_dataset` con el archivo `area_codes.csv` esté en el mismo directorio.
3. Ejecuta el programa:
   ```
   python arg_phone_standardizer.py
   ```
4. Sigue las instrucciones en la interfaz gráfica para seleccionar el archivo de entrada y la carpeta de salida.

## Notas

- El archivo de entrada debe ser un CSV con una columna llamada 'phone'.
- El programa generará dos archivos de salida: uno con números válidos y otro con números inválidos.
