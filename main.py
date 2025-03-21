import tkinter as tk
from tkinter import ttk
from productos import lista_productos


class FruberApp:
    def __init__(self, root): #Metodo constructor
        self.root = root
        self.root.title("Fruber - Caja Registradora") # Titulo de la ventana
        self.root.geometry("900x600")    # Tamaño de la ventana
        self.root.resizable(False, True) # No redimensionable

        # Inicializar datos
        self.productos = lista_productos


        # llamar la interfaz
        self.configurar_interfaz()




    def configurar_interfaz(self):
        """Configura todos los elementos de la interfaz gráfica"""

        # frame (contenedor) dentro de la ventana principal con un margen de 20 píxeles y se expande para llenar toda la ventana
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Título de la aplicación
        titulo = ttk.Label(main_frame, text="Fruber - Caja Registradora", font=("Arial", 18, "bold"))
        titulo.grid(row=0, column=0, columnspan=2, pady=(0, 20))




        # Marco izquierdo para lista de productos
        productos_frame = ttk.LabelFrame(main_frame, text="Lista de Productos", padding="10")
        productos_frame.grid(row=1, column=0, sticky="nsew", padx=(0, 10))

        # Lista de productos
        self.crear_lista_productos(productos_frame)



        # Marco derecho para carrito de compras
        carrito_frame = ttk.LabelFrame(main_frame, text="Carrito de Compras", padding="10")
        carrito_frame.grid(row=1, column=1, sticky="nsew")

        # Lista del carrito de compras
        self.crear_lista_carrito(carrito_frame)



        # Marco para cantidad y botones
        cantidad_frame = ttk.Frame(productos_frame, padding="10")
        cantidad_frame.pack(fill=tk.X, pady=(10, 0))

        # Etiqueta y entrada para cantidad
        cantidad_label = ttk.Label(cantidad_frame, text="Cantidad:")
        cantidad_label.pack(side=tk.LEFT, padx=(0, 5))

        #Creamos entrada de texto para la etiqueta cantidad
        self.cantidad_var = tk.StringVar()
        cantidad_entry = ttk.Entry(cantidad_frame, textvariable=self.cantidad_var, width=10)
        cantidad_entry.pack(side=tk.LEFT, padx=(0, 10))

        # Botón para agregar al carrito
        agregar_btn = ttk.Button(cantidad_frame, text="Agregar al carrito", command=self.agregar_al_carrito)
        agregar_btn.pack(side=tk.LEFT)





    def crear_lista_productos(self, parent_frame):
        """Crea la lista de productos disponibles"""

        # Crear un frame para contener nuestra tabla (Lista de productos)
        frame = ttk.Frame(parent_frame)
        frame.pack(fill=tk.BOTH, expand=True)

        # Columnas
        columns = ('id', 'nombre', 'precio', 'stock')

        # Crear Treeview para mostar los productos en una tabla
        self.productos_tree = ttk.Treeview(frame, columns=columns, show='headings', height=15)

        # Definir encabezados
        self.productos_tree.heading('id', text='ID')
        self.productos_tree.heading('nombre', text='Producto')
        self.productos_tree.heading('precio', text='Precio')
        self.productos_tree.heading('stock', text='Stock')

        # Definir anchos de columna
        self.productos_tree.column('id', width=50, anchor=tk.CENTER)
        self.productos_tree.column('nombre', width=150)
        self.productos_tree.column('precio', width=100, anchor=tk.E)
        self.productos_tree.column('stock', width=100, anchor=tk.E)

        # Añadir barras de desplazamiento
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.productos_tree.yview)
        self.productos_tree.configure(yscrollcommand=scrollbar.set)

        # Empaquetar el Treeview (Tabla(Lista de productos)) dentro del frame
        self.productos_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Llenar con datos
        self.actualizar_lista_productos()




    def actualizar_lista_productos(self):
        """Actualiza la lista de productos en la interfaz"""
        # Limpiar la lista actual
        for item in self.productos_tree.get_children():
            self.productos_tree.delete(item)


        # Añadir productos
        for producto in self.productos:
            self.productos_tree.insert('', tk.END, values=(
                producto.id,
                producto.nombre,
                f"${producto.precio:.2f}",
                producto.stock
            ))




    def crear_lista_carrito(self, parent_frame):
        """Crea la lista del carrito de compras"""

        # Crear un frame para la lista
        frame = ttk.Frame(parent_frame)
        frame.pack(fill=tk.BOTH, expand=True)

        # Columnas
        columns = ('producto', 'cantidad', 'subtotal')

        # Crear Treeview
        self.carrito_tree = ttk.Treeview(frame, columns=columns, show='headings', height=15)

        # Definir encabezados
        self.carrito_tree.heading('producto', text='Producto')
        self.carrito_tree.heading('cantidad', text='Cantidad')
        self.carrito_tree.heading('subtotal', text='Subtotal')

        # Definir anchos de columna
        self.carrito_tree.column('producto', width=150)
        self.carrito_tree.column('cantidad', width=100, anchor=tk.CENTER)
        self.carrito_tree.column('subtotal', width=100, anchor=tk.E)

        # Añadir barras de desplazamiento
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.carrito_tree.yview)
        self.carrito_tree.configure(yscrollcommand=scrollbar.set)

        # Empaquetar
        self.carrito_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def agregar_al_carrito(self):
        """Agrega un producto seleccionado al carrito"""








if __name__ == "__main__":

    root = tk.Tk()
    app = FruberApp(root)
    root.mainloop() # inicia el bucle principal de eventos de Tkinter