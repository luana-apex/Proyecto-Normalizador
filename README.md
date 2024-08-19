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



## Creación del archivo ejecutable (.exe)

Para crear un archivo ejecutable (.exe) de este programa, seguiremos estos pasos utilizando PyInstaller. Este proceso permitirá que otros usuarios ejecuten el programa sin necesidad de tener Python instalado.

### Requisitos previos

1. Python 3.x instalado en tu sistema
2. pip (gestor de paquetes de Python)

### Pasos para crear el ejecutable

1. Instala PyInstaller:
   Abre una terminal o símbolo del sistema y ejecuta:
   ```
   pip install pyinstaller
   ```

2. Navega al directorio del proyecto:
   ```
   cd ruta/a/tu/proyecto
   ```

3. Crea el ejecutable:
   Ejecuta el siguiente comando:
   ```
   pyinstaller --onefile --windowed --add-data "area_codes_dataset/area_codes.csv;area_codes_dataset" --add-data "icon.ico;." arg_phone_standardizer.py
   ```

   Explicación de las opciones:
   - `--onefile`: Crea un único archivo ejecutable.
   - `--windowed`: Crea una aplicación de Windows sin consola.
   - `--add-data`: Incluye archivos adicionales necesarios.

4. Encuentra tu ejecutable:
   El archivo .exe se creará en la carpeta `dist` dentro del directorio de tu proyecto.

### Estructura de archivos

Asegúrate de que tu proyecto tenga la siguiente estructura antes de crear el ejecutable:
tu_proyecto/
│
├── arg_phone_standardizer.py
├── icon.ico
└── area_codes_dataset/
└── area_codes.csv

### Notas adicionales

- Si modificas el código o los archivos de datos, deberás volver a crear el ejecutable.
- El proceso de creación puede tardar unos minutos.
- El archivo ejecutable resultante será significativamente más grande que el script original, ya que incluye todas las dependencias necesarias.

### Distribución

Para distribuir tu programa:

1. Comparte el archivo .exe generado en la carpeta `dist`.
2. Opcionalmente, incluye este README para proporcionar instrucciones de uso.

### Solución de problemas

Si los usuarios encuentran problemas al ejecutar el .exe, pueden intentar:

1. Ejecutar como administrador.
2. Desbloquear el archivo en las propiedades de Windows.
3. Añadir una excepción en su software antivirus.
4. Mover el archivo a una ubicación diferente antes de ejecutarlo.
