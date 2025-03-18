import pandas as pd
from sorting_algorithms import SortingAlgorithms

class DataProcessor:
    """
    Clase para procesar y ordenar datos obtenidos de una API.
    """
    
    def __init__(self, data=None):
        """
        Inicializa el procesador de datos con un dataset opcional.
        
        Args:
            data (pandas.DataFrame, optional): Dataset inicial a procesar.
        """
        self.data = data
        self.sorted_data = None
        self.sorting_algorithms = {
            "Burbuja": SortingAlgorithms.bubble_sort,
            "Selección": SortingAlgorithms.selection_sort,
            "Inserción": SortingAlgorithms.insertion_sort
        }
        
    def set_data(self, data):
        """
        Establece un nuevo dataset para procesar.
        
        Args:
            data (pandas.DataFrame): Nuevo dataset.
        """
        self.data = data
        self.sorted_data = None
        
    def get_data(self):
        """
        Obtiene el dataset actual.
        
        Returns:
            pandas.DataFrame: Dataset actual (ordenado si está disponible, original en caso contrario).
        """
        if self.sorted_data is not None:
            return self.sorted_data
        return self.data
        
    def get_available_algorithms(self):
        """
        Obtiene la lista de algoritmos de ordenamiento disponibles.
        
        Returns:
            list: Nombres de los algoritmos disponibles.
        """
        return list(self.sorting_algorithms.keys())
        
    def sort_data(self, column, algorithm_name, ascending=True):
        """
        Ordena el dataset según la columna y algoritmo especificados.
        
        Args:
            column (str): Nombre de la columna por la cual ordenar.
            algorithm_name (str): Nombre del algoritmo a utilizar.
            ascending (bool): True para orden ascendente, False para descendente.
            
        Returns:
            pandas.DataFrame: Dataset ordenado.
        """
        if self.data is None:
            print("No hay datos para ordenar.")
            return None
            
        if algorithm_name not in self.sorting_algorithms:
            print(f"Algoritmo '{algorithm_name}' no disponible.")
            return self.data
            
        # Convertir DataFrame a lista de diccionarios para los algoritmos de ordenamiento
        records = self.data.to_dict('records')
        
        # Aplicar el algoritmo de ordenamiento seleccionado
        algorithm = self.sorting_algorithms[algorithm_name]
        sorted_records = algorithm(records, column, ascending)
        
        # Convertir de vuelta a DataFrame
        self.sorted_data = pd.DataFrame(sorted_records)
        return self.sorted_data