class StockInsuficienteError(Exception):
    """Excepción que se lanza cuando no hay suficiente stock de un producto"""
    def __init__(self, producto, cantidad_disponible, cantidad_solicitada):
        self.producto = producto
        self.cantidad_disponible = cantidad_disponible
        self.cantidad_solicitada = cantidad_solicitada
        mensaje = f"Stock insuficiente para '{producto}'. Disponible: {cantidad_disponible}, Solicitado: {cantidad_solicitada}"
        super().__init__(mensaje)


class CantidadInvalidaError(Exception):
    """Excepción que se lanza cuando se ingresa una cantidad inválida"""
    def __init__(self, mensaje="Debe ingresar una cantidad válida (número entero positivo)"):
        super().__init__(mensaje)


class ProductoNoSeleccionadoError(Exception):
    """Excepción que se lanza cuando no se selecciona un producto"""
    def __init__(self, mensaje="Debe seleccionar un producto de la lista"):
        super().__init__(mensaje)


class CedulaInvalidaError(Exception):
    """Excepción que se lanza cuando se ingresa una cédula inválida"""
    def __init__(self, mensaje="Debe ingresar una cédula válida"):
        super().__init__(mensaje)


class CarritoVacioError(Exception):
    """Excepción que se lanza cuando se intenta finalizar una compra con el carrito vacío"""
    def __init__(self, mensaje="No hay productos en el carrito para finalizar la compra"):
        super().__init__(mensaje)