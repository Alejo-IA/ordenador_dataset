from api_handler import APIHandler
from data_processor import DataProcessor
from ui_manager import UIManager
import os
from dotenv import load_dotenv

def main():
    """
    Función principal que inicializa y ejecuta la aplicación.
    """
    # Cargar variables de entorno desde archivo .env
    load_dotenv()
    
    # Obtener la API key desde la variable de entorno
    api_key = os.environ.get("API_KEY", "")
    
    # Inicializar el manejador de API
    api_handler = APIHandler(api_key=api_key)
    
    # Inicializar el procesador de datos
    data_processor = DataProcessor()
    
    # Inicializar y ejecutar la interfaz gráfica
    ui = UIManager(api_handler, data_processor)
    ui.run()

if __name__ == "__main__":
    main()
    