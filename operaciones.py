from excepciones import StockInsuficienteError, CantidadInvalidaError

class ItemCarrito:
    """Clase para representar un item en el carrito de compras"""
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad
        self.subtotal = producto.precio * cantidad

    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad} = ${self.subtotal:.2f}"


class Carrito:
    """Clase para manejar el carrito de compras"""
    def __init__(self):
        self.items = []
        self.total = 0.0

    def agregar_producto(self, producto, cantidad):
        """Agrega un producto al carrito verificando el stock"""
        try:
            # Validar que la cantidad sea válida
            if not isinstance(cantidad, int) or cantidad <= 0:
                raise CantidadInvalidaError()

            # Verificar stock suficiente
            if cantidad > producto.stock:
                raise StockInsuficienteError(producto.nombre, producto.stock, cantidad)

            # Agregar al carrito
            item = ItemCarrito(producto, cantidad)
            self.items.append(item)
            self.total += item.subtotal

            # Actualizar stock
            producto.actualizar_stock(cantidad)

            return True
        except Exception as e:
            # Propagar la excepción
            raise e

    def eliminar_producto(self, indice):
        """Elimina un producto del carrito y restaura el stock"""
        if 0 <= indice < len(self.items):
            item = self.items[indice]
            # Restaurar stock
            item.producto.stock += item.cantidad
            # Actualizar total
            self.total -= item.subtotal
            # Eliminar del carrito
            self.items.pop(indice)
            return True
        return False

    def vaciar_carrito(self):
        """Vacía el carrito de compras"""
        self.items = []
        self.total = 0.0

class HistorialVentas:
    """Clase para manejar el historial de ventas"""
    def __init__(self):
        self.ventas = []
        self.ganancia_total = 0.0

    def registrar_venta(self, carrito):
        """Registra una venta en el historial"""
        if carrito.items:
            # Guardar los items del carrito en el historial
            self.ventas.extend(carrito.items)
            # Actualizar ganancia total
            self.ganancia_total += carrito.total
            return True
        return False

    def obtener_ventas(self):
        """Retorna la lista de ventas"""
        return self.ventas

    def obtener_ganancia_total(self):
        """Retorna la ganancia total"""
        return self.ganancia_total

