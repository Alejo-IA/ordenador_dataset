import requests
import pandas as pd

class APIHandler:
    """
    Clase para manejar el consumo de una API y obtener un dataset.
    """
    
    def __init__(self, api_url=None, api_key=None):
        """
        Inicializa el manejador de API con una URL opcional y una API key opcional.
        
        Args:
            api_url (str, optional): URL de la API a consumir. Si no se proporciona, se usará una API por defecto.
            api_key (str, optional): Clave API para la autenticación.
        """
        self.api_url = api_url if api_url else "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1"
        self.api_key = api_key
        self.data = None
        
    def set_api_url(self, url):
        """
        Establece una nueva URL para la API.
        
        Args:
            url (str): Nueva URL de la API.
        """
        self.api_url = url
        
    def set_api_key(self, api_key):
        """
        Establece una nueva API key para la autenticación.
        
        Args:
            api_key (str): Nueva API key.
        """
        self.api_key = api_key
        
    def fetch_data(self):
        """
        Realiza la petición a la API y obtiene los datos.
        
        Returns:
            pandas.DataFrame: DataFrame con los datos obtenidos de la API, o None si hay error.
        """
        try:
            # Configurar headers con la API key si está disponible
            headers = {}
            if self.api_key:
                headers['Authorization'] = f'Bearer {self.api_key}'
                # Algunas APIs utilizan otros formatos de autenticación
                # headers['X-API-Key'] = self.api_key
            
            response = requests.get(self.api_url, headers=headers)
            response.raise_for_status()  # Verifica si la petición fue exitosa
            data = response.json()
            
            # Convertir a DataFrame de pandas para mejor manejo
            df = pd.DataFrame(data)
            
            # Verificar que el dataset contiene al menos dos variables numéricas
            numeric_columns = df.select_dtypes(include=['number']).columns
            if len(numeric_columns) < 2:
                print("El dataset debe contener al menos dos variables numéricas.")
                return None
            
            self.data = df
            return df
            
        except requests.exceptions.RequestException as e:
            print(f"Error al consumir la API: {e}")
            return None
            
    def get_numeric_columns(self):
        """
        Obtiene las columnas numéricas del dataset.
        
        Returns:
            list: Lista de nombres de columnas numéricas.
        """
        if self.data is not None:
            return list(self.data.select_dtypes(include=['number']).columns)
        return []
        
    def get_data(self):
        """
        Obtiene el dataset actual.
        
        Returns:
            pandas.DataFrame: Dataset actual.
        """
        return self.data