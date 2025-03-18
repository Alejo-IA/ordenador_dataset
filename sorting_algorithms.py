class SortingAlgorithms:
    """
    Clase que implementa diferentes algoritmos de ordenamiento.
    """
    
    @staticmethod
    def bubble_sort(data, column, ascending=True):
        """
        Implementación del algoritmo de ordenamiento burbuja.
        
        Args:
            data (list): Lista de diccionarios o registros a ordenar.
            column (str): Nombre de la columna por la cual ordenar.
            ascending (bool): True para orden ascendente, False para descendente.
            
        Returns:
            list: Lista ordenada de registros.
        """
        result = data.copy()
        n = len(result)
        
        for i in range(n):
            for j in range(0, n - i - 1):
                # Comparación para orden ascendente o descendente
                condition = result[j][column] > result[j + 1][column] if ascending else result[j][column] < result[j + 1][column]
                
                if condition:
                    result[j], result[j + 1] = result[j + 1], result[j]
                    
        return result

    @staticmethod
    def selection_sort(data, column, ascending=True):
        """
        Implementación del algoritmo de ordenamiento por selección.
        
        Args:
            data (list): Lista de diccionarios o registros a ordenar.
            column (str): Nombre de la columna por la cual ordenar.
            ascending (bool): True para orden ascendente, False para descendente.
            
        Returns:
            list: Lista ordenada de registros.
        """
        result = data.copy()
        n = len(result)
        
        for i in range(n):
            # Encontrar el valor mínimo/máximo en el resto de la lista
            idx = i
            for j in range(i + 1, n):
                # Comparación para orden ascendente o descendente
                condition = result[j][column] < result[idx][column] if ascending else result[j][column] > result[idx][column]
                
                if condition:
                    idx = j
                    
            # Intercambiar el elemento encontrado con el primer elemento sin ordenar
            result[i], result[idx] = result[idx], result[i]
                    
        return result

    @staticmethod
    def insertion_sort(data, column, ascending=True):
        """
        Implementación del algoritmo de ordenamiento por inserción.
        
        Args:
            data (list): Lista de diccionarios o registros a ordenar.
            column (str): Nombre de la columna por la cual ordenar.
            ascending (bool): True para orden ascendente, False para descendente.
            
        Returns:
            list: Lista ordenada de registros.
        """
        result = data.copy()
        n = len(result)
        
        for i in range(1, n):
            key = result[i]
            j = i - 1
            
            # Comparación para orden ascendente o descendente
            condition = key[column] < result[j][column] if ascending else key[column] > result[j][column]
            
            while j >= 0 and condition:
                result[j + 1] = result[j]
                j -= 1
                if j >= 0:
                    condition = key[column] < result[j][column] if ascending else key[column] > result[j][column]
                    
            result[j + 1] = key
                    
        return result