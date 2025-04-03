import tkinter as tk
from tkinter import ttk,messagebox
from productos import lista_productos
from excepciones import StockInsuficienteError, CantidadInvalidaError, ProductoNoSeleccionadoError, CarritoVacioError
from operaciones import Carrito, HistorialVentas


class FruberApp:
    def __init__(self, root): #Metodo constructor
        self.root = root
        self.root.title("Fruber - Caja Registradora") # Titulo de la ventana
        self.root.geometry("900x600")    # Tamaño de la ventana
        self.root.resizable(False, True) # No redimensionable

        # Inicializar datos
        self.productos = lista_productos
        self.carrito = Carrito()
        self.historial = HistorialVentas()


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

        # Botón para eliminar del carrito
        eliminar_btn = ttk.Button(carrito_frame, text="Eliminar producto", command=self.eliminar_del_carrito)
        eliminar_btn.pack(fill=tk.X, pady=(10, 0))

        # Etiqueta para el total
        self.total_var = tk.StringVar(value="Total: $0.00")
        total_label = ttk.Label(carrito_frame, textvariable=self.total_var, font=("Arial", 12, "bold"))
        total_label.pack(fill=tk.X, pady=(10, 0))



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



        # Botones inferiores
        botones_frame = ttk.Frame(main_frame, padding="10")
        botones_frame.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(10, 0))

        finalizar_btn = ttk.Button(botones_frame, text="Finalizar Compra", command=self.finalizar_compra)
        finalizar_btn.pack(side=tk.LEFT, padx=(0, 10))

        historial_btn = ttk.Button(botones_frame, text="Historial", command=self.mostrar_historial)
        historial_btn.pack(side=tk.LEFT)





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
        try:
            # Obtener producto seleccionado
            seleccion = self.productos_tree.selection()
            if not seleccion:
                raise ProductoNoSeleccionadoError()

            item_id = seleccion[0]
            producto_id = int(self.productos_tree.item(item_id, 'values')[0])

            # Buscar el producto por ID
            producto = next((p for p in self.productos if p.id == producto_id), None)
            if not producto:
                raise Exception("Producto no encontrado")

            # Obtener cantidad
            try:
                cantidad = int(self.cantidad_var.get())
            except ValueError:
                raise CantidadInvalidaError()

            # Agregar al carrito
            self.carrito.agregar_producto(producto, cantidad)

            # Actualizar interfaces
            self.actualizar_lista_productos()
            self.actualizar_carrito()

            # Limpiar campo de cantidad
            self.cantidad_var.set("")

        except (StockInsuficienteError, CantidadInvalidaError, ProductoNoSeleccionadoError) as e:
            messagebox.showerror("Error", e.message)
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {str(e)}")


    def actualizar_carrito(self):
        """Actualiza la lista del carrito en la interfaz"""
        # Limpiar la lista actual
        for item in self.carrito_tree.get_children():
            self.carrito_tree.delete(item)

        # Añadir items del carrito
        for item in self.carrito.items:
            self.carrito_tree.insert('', tk.END, values=(
                item.producto.nombre,
                item.cantidad,
                f"${item.subtotal:.2f}"
            ))

        # Actualizar total
        self.total_var.set(f"Total: ${self.carrito.total:.2f}")



    def eliminar_del_carrito(self):
        """Elimina un producto seleccionado del carrito"""
        try:
            # Obtener item seleccionado
            seleccion = self.carrito_tree.selection()
            if not seleccion:
                raise Exception("Seleccione un producto del carrito para eliminar")

            # Obtener índice (posición en la lista)
            indice = self.carrito_tree.index(seleccion[0])

            # Eliminar del carrito
            if self.carrito.eliminar_producto(indice):
                # Actualizar interfaces
                self.actualizar_lista_productos()
                self.actualizar_carrito()

        except Exception as e:
            messagebox.showerror("Error", str(e))



    def finalizar_compra(self):
        """Finaliza la compra actual"""
        try:
            # Verificar que el carrito no esté vacío
            if not self.carrito.items:
                raise CarritoVacioError()

            # Calcular total
            total = self.carrito.total

            # Registrar en historial
            self.historial.registrar_venta(self.carrito)

            # Mostrar resumen
            resumen = "Compra finalizada con éxito\n\n"
            resumen += f"Total: ${total:.2f}\n\n"
            resumen += "Productos comprados:\n"
            for item in self.carrito.items:
                resumen += f"- {item.producto.nombre} x {item.cantidad} = ${item.subtotal:.2f}\n"

            messagebox.showinfo("Resumen de Compra", resumen)

            # Vaciar carrito
            self.carrito.vaciar_carrito()

            # Actualizar interfaz
            self.actualizar_carrito()

        except CarritoVacioError as e:
            messagebox.showerror("Error", e.message)
        except Exception as e:
            messagebox.showerror("Error", f"Error al finalizar la compra: {str(e)}")




    def mostrar_historial(self):
        """Muestra el historial de ventas"""
        # Crear ventana de historial
        historial_window = tk.Toplevel(self.root)
        historial_window.title("Historial de Ventas")
        historial_window.geometry("600x400")
        historial_window.transient(self.root)
        historial_window.grab_set()

        # Frame principal
        main_frame = ttk.Frame(historial_window, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Título
        titulo = ttk.Label(main_frame, text="Historial de Ventas", font=("Arial", 14, "bold"))
        titulo.pack(pady=(0, 20))

        # Crear frame para la tabla
        table_frame = ttk.Frame(main_frame)
        table_frame.pack(fill=tk.BOTH, expand=True)

        # Columnas
        columns = ('producto', 'cantidad', 'precio')

        # Crear Treeview
        historial_tree = ttk.Treeview(table_frame, columns=columns, show='headings')

        # Definir encabezados
        historial_tree.heading('producto', text='Producto')
        historial_tree.heading('cantidad', text='Cantidad')
        historial_tree.heading('precio', text='Precio Total')

        # Definir anchos de columna
        historial_tree.column('producto', width=250)
        historial_tree.column('cantidad', width=100, anchor=tk.CENTER)
        historial_tree.column('precio', width=150, anchor=tk.E)

        # Añadir barras de desplazamiento
        scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=historial_tree.yview)
        historial_tree.configure(yscrollcommand=scrollbar.set)

        # Empaquetar
        historial_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Llenar con datos del historial
        ventas = self.historial.obtener_ventas()
        for item in ventas:
            historial_tree.insert('', tk.END, values=(
                item.producto.nombre,
                item.cantidad,
                f"${item.subtotal:.2f}"
            ))

        # Mostrar ganancia total
        ganancia_total = self.historial.obtener_ganancia_total()
        ganancia_label = ttk.Label(
            main_frame,
            text=f"Ganancia Total: ${ganancia_total:.2f}",
            font=("Arial", 12, "bold")
        )
        ganancia_label.pack(pady=(10, 0))

        # Botón de cerrar
        cerrar_btn = ttk.Button(main_frame, text="Cerrar", command=historial_window.destroy)
        cerrar_btn.pack(pady=(10, 0))





if __name__ == "__main__":

    root = tk.Tk()
    app = FruberApp(root)
    root.mainloop() # inicia el bucle principal de eventos de Tkinter