# Aplicación de Ordenamiento de Datos de API

Esta aplicación permite consumir datos de una API, visualizarlos y ordenarlos utilizando diferentes algoritmos de ordenamiento.

## Características

- Consumo de datos de API (por defecto, CoinGecko para datos de criptomonedas)
- Visualización de datos en una tabla
- Selección de variables numéricas para ordenar
- Implementación de tres algoritmos de ordenamiento:
  - Burbuja
  - Selección
  - Inserción
- Ordenamiento ascendente o descendente
- Visualización gráfica de los datos

## Requisitos

- Python 3.7+
- Bibliotecas requeridas:
  - requests
  - pandas
  - numpy
  - matplotlib
  - tkinter (incluido con Python)

## Instalación

1. Clonar este repositorio:
```
git clone https://github.com/tu-usuario/proyecto-ordenamiento-api.git
cd proyecto-ordenamiento-api
```

2. Instalar las dependencias:
```
pip install -r requirements.txt
```

## Uso

1. Ejecutar la aplicación:
```
python main.py
```

2. En la interfaz:
   - Hacer clic en "Cargar Datos de API" para obtener los datos
   - Seleccionar la columna numérica para ordenar
   - Elegir el algoritmo de ordenamiento
   - Seleccionar ordenamiento ascendente o descendente
   - Hacer clic en "Ordenar Datos" para aplicar el ordenamiento

## Estructura del Proyecto

- `main.py`: Archivo principal de la aplicación
- `api_handler.py`: Clase para consumir la API
- `data_processor.py`: Clase para procesar y ordenar datos
- `sorting_algorithms.py`: Implementación de algoritmos de ordenamiento
- `ui_manager.py`: Gestión de la interfaz gráfica

## Implementación

La aplicación está desarrollada siguiendo principios de Programación Orientada a Objetos:

- `APIHandler`: Encargada de consumir la API y obtener los datos
- `SortingAlgorithms`: Implementa diversos algoritmos de ordenamiento
- `DataProcessor`: Procesa y ordena los datos
- `UIManager`: Gestiona la interfaz gráfica

## Explicación de los Algoritmos de Ordenamiento

1. **Bubble Sort (Ordenamiento Burbuja)**:
   - Compara cada par de elementos adyacentes
   - Intercambia elementos si están en el orden incorrecto
   - Complejidad: O(n²)

2. **Selection Sort (Ordenamiento por Selección)**:
   - Busca el elemento mínimo/máximo en cada iteración
   - Lo coloca en su posición correcta
   - Complejidad: O(n²)

3. **Insertion Sort (Ordenamiento por Inserción)**:
   - Construye una sublista ordenada elemento por elemento
   - Inserta cada elemento en la posición correcta dentro de la sublista
   - Complejidad: O(n²)