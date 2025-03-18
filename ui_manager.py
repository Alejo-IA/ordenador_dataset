import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class UIManager:
    """
    Clase para gestionar la interfaz gráfica de la aplicación.
    """
    
    def __init__(self, api_handler, data_processor):
        """
        Inicializa el administrador de UI con los manejadores de API y datos.
        
        Args:
            api_handler: Instancia de APIHandler para obtener datos.
            data_processor: Instancia de DataProcessor para procesar datos.
        """
        self.api_handler = api_handler
        self.data_processor = data_processor
        
        # Configuración de la ventana principal
        self.root = tk.Tk()
        self.root.title("Ordenador de Datos")
        self.root.geometry("1200x800")
        self.root.configure(bg="#f0f0f0")
        
        self.setup_ui()
        
    def setup_ui(self):
        """Configura todos los elementos de la interfaz gráfica."""
        # Frame principal
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Frame para configuración de API
        api_frame = ttk.LabelFrame(main_frame, text="Configuración de API", padding=10)
        api_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # URL de API
        api_url_label = ttk.Label(api_frame, text="URL de API:")
        api_url_label.grid(row=0, column=0, padx=5, pady=5)
        
        self.api_url_var = tk.StringVar(value=self.api_handler.api_url)
        api_url_entry = ttk.Entry(api_frame, textvariable=self.api_url_var, width=50)
        api_url_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # API Key
        api_key_label = ttk.Label(api_frame, text="API Key:")
        api_key_label.grid(row=1, column=0, padx=5, pady=5)
        
        self.api_key_var = tk.StringVar()
        api_key_entry = ttk.Entry(api_frame, textvariable=self.api_key_var, width=50, show="*")
        api_key_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Botón para actualizar configuración de API
        update_api_button = ttk.Button(api_frame, text="Actualizar Configuración", command=self.update_api_config)
        update_api_button.grid(row=1, column=2, padx=5, pady=5)
        
        # Frame superior para controles
        control_frame = ttk.LabelFrame(main_frame, text="Controles", padding=10)
        control_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Botón para cargar datos
        fetch_button = ttk.Button(control_frame, text="Cargar Datos de API", command=self.fetch_data)
        fetch_button.grid(row=0, column=0, padx=5, pady=5)
        
        # Selector de columna
        self.column_label = ttk.Label(control_frame, text="Columna a ordenar:")
        self.column_label.grid(row=0, column=1, padx=5, pady=5)
        
        self.column_var = tk.StringVar()
        self.column_dropdown = ttk.Combobox(control_frame, textvariable=self.column_var, state="readonly")
        self.column_dropdown.grid(row=0, column=2, padx=5, pady=5)
        
        # Selector de algoritmo
        self.algorithm_label = ttk.Label(control_frame, text="Algoritmo:")
        self.algorithm_label.grid(row=0, column=3, padx=5, pady=5)
        
        self.algorithm_var = tk.StringVar()
        self.algorithm_dropdown = ttk.Combobox(control_frame, textvariable=self.algorithm_var, state="readonly")
        self.algorithm_dropdown.grid(row=0, column=4, padx=5, pady=5)
        self.algorithm_dropdown["values"] = self.data_processor.get_available_algorithms()
        self.algorithm_dropdown.current(0)
        
        # Selector de dirección de ordenamiento
        self.direction_var = tk.BooleanVar(value=True)
        self.asc_radio = ttk.Radiobutton(control_frame, text="Ascendente", variable=self.direction_var, value=True)
        self.asc_radio.grid(row=0, column=5, padx=5, pady=5)
        
        self.desc_radio = ttk.Radiobutton(control_frame, text="Descendente", variable=self.direction_var, value=False)
        self.desc_radio.grid(row=0, column=6, padx=5, pady=5)
        
        # Botón para ordenar
        sort_button = ttk.Button(control_frame, text="Ordenar Datos", command=self.sort_data)
        sort_button.grid(row=0, column=7, padx=5, pady=5)
        
        # Frame para tabla de datos
        data_frame = ttk.LabelFrame(main_frame, text="Datos", padding=10)
        data_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Crear treeview para mostrar datos
        self.tree_frame = ttk.Frame(data_frame)
        self.tree_frame.pack(fill=tk.BOTH, expand=True)
        
        self.tree_scroll = ttk.Scrollbar(self.tree_frame)
        self.tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.tree = ttk.Treeview(self.tree_frame, yscrollcommand=self.tree_scroll.set)
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        self.tree_scroll.config(command=self.tree.yview)
        
        # Frame para gráfico
        self.graph_frame = ttk.LabelFrame(main_frame, text="Visualización", padding=10)
        self.graph_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Configurar selector de columnas después de cargar los datos
        self.column_dropdown.bind("<<ComboboxSelected>>", self.update_graph)
        
    def update_api_config(self):
        """Actualiza la configuración de la API con la URL y API key proporcionadas."""
        api_url = self.api_url_var.get().strip()
        api_key = self.api_key_var.get().strip()
        
        if api_url:
            self.api_handler.set_api_url(api_url)
        
        if api_key:
            self.api_handler.set_api_key(api_key)
            
        messagebox.showinfo("Configuración Actualizada", "La configuración de la API ha sido actualizada")
        
    def fetch_data(self):
        """Obtiene datos de la API y actualiza la interfaz."""
        data = self.api_handler.fetch_data()
        if data is not None:
            # Actualizar el procesador de datos
            self.data_processor.set_data(data)
            
            # Actualizar el selector de columnas
            numeric_columns = self.api_handler.get_numeric_columns()
            self.column_dropdown["values"] = numeric_columns
            if numeric_columns:
                self.column_dropdown.current(0)
            
            # Actualizar la tabla de datos
            self.update_table(data)
            
            # Actualizar el gráfico
            self.update_graph()
            
            messagebox.showinfo("Éxito", "Datos cargados correctamente")
        else:
            messagebox.showerror("Error", "No se pudieron cargar los datos")
            
    def sort_data(self):
        """Ordena los datos según las selecciones del usuario."""
        column = self.column_var.get()
        algorithm = self.algorithm_var.get()
        ascending = self.direction_var.get()
        
        if not column:
            messagebox.showerror("Error", "Seleccione una columna para ordenar")
            return
            
        sorted_data = self.data_processor.sort_data(column, algorithm, ascending)
        if sorted_data is not None:
            self.update_table(sorted_data)
            self.update_graph()
            messagebox.showinfo("Éxito", f"Datos ordenados usando algoritmo '{algorithm}'")
            
    def update_table(self, dataframe):
        """
        Actualiza la tabla con los datos proporcionados.
        
        Args:
            dataframe (pandas.DataFrame): Datos a mostrar en la tabla.
        """
        # Limpiar tabla existente
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        # Configurar columnas
        self.tree["columns"] = list(dataframe.columns)
        self.tree["show"] = "headings"
        
        for column in dataframe.columns:
            self.tree.heading(column, text=column)
            # Ajustar ancho de columna
            col_width = max(50, len(str(column)) * 10)
            self.tree.column(column, width=col_width)
            
        # Insertar datos
        for _, row in dataframe.head(50).iterrows():  # Mostrar solo las primeras 50 filas para mejorar rendimiento
            self.tree.insert("", tk.END, values=list(row))
            
    def update_graph(self, event=None):
        """Actualiza el gráfico basado en la columna seleccionada."""
        # Limpiar gráfico existente
        for widget in self.graph_frame.winfo_children():
            widget.destroy()
            
        column = self.column_var.get()
        if not column or self.data_processor.get_data() is None:
            return
            
        data = self.data_processor.get_data()
        
        # Crear figura y agregar subgráfico
        fig, ax = plt.subplots(figsize=(10, 5))
        
        # Limitar a los primeros 30 registros para mejor visualización
        display_data = data.head(20)
        
        # Determinar el tipo de gráfico según los datos
        if "name" in data.columns:
            # Si hay una columna de nombres, usarla como etiqueta
            ax.bar(display_data["name"], display_data[column])
            plt.xticks(rotation=45, ha="right")
        else:
            # Usar índices como etiquetas
            ax.bar(range(len(display_data)), display_data[column])
            ax.set_xticks(range(len(display_data)))
            ax.set_xticklabels([f"Item {i+1}" for i in range(len(display_data))])
            plt.xticks(rotation=45, ha="right")
            
        ax.set_title(f"Visualización de la columna '{column}'")
        ax.set_ylabel(column)
        plt.tight_layout()
        
        # Agregar gráfico a la interfaz
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            
    def run(self):
        """Ejecuta el bucle principal de la aplicación."""
        self.root.mainloop()