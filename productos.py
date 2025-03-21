# La clase productos define cada uno de lo proctos con sus caracteristicas
class Producto:
    def __init__(self,id,nombre,precio,stock):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

# El metodo str define como texto a los atributos del objeto (nombre, precio, stock)
    def __str__(self):
        return f"{self.nombre} ${self.precio} -Stock: {self.stock}"

# Funcion para actualizar el stock en cada venta
    def actualizar_stock(self,cantidad):
        self.stock -= cantidad

# Lista que contiene 50 objetos Producto ya creados. Cada uno representa un tipo de fruta o verdura con su ID, nombre, precio y stock inicial.
lista_productos = [
    Producto(1, "Manzana (kg)", 3500, 50),
    Producto(2, "Banano (kg)", 2500, 40),
    Producto(3, "Naranja (kg)", 3000, 45),
    Producto(4, "Pera (kg)", 4000, 30),
    Producto(5, "Fresa (kg)", 6000, 25),
    Producto(6, "Uva (kg)", 7000, 20),
    Producto(7, "Tomate (kg)", 2800, 60),
    Producto(8, "Cebolla (kg)", 2000, 55),
    Producto(9, "Zanahoria (kg)", 1800, 70),
    Producto(10, "Papa (kg)", 1500, 80),
    Producto(11, "Sandía (kg)", 2500, 35),
    Producto(12, "Melón (kg)", 3200, 40),
    Producto(13, "Piña (kg)", 2800, 30),
    Producto(14, "Mango (kg)", 3500, 50),
    Producto(15, "Papaya (kg)", 3000, 45),
    Producto(16, "Limón (kg)", 2000, 55),
    Producto(17, "Calabacín (kg)", 1800, 70),
    Producto(18, "Aguacate (kg)", 4000, 25),
    Producto(19, "Pepino (kg)", 2400, 60),
    Producto(20, "Lechuga (kg)", 2200, 65),
    Producto(21, "Espinaca (kg)", 2600, 55),
    Producto(22, "Coliflor (kg)", 2800, 50),
    Producto(23, "Brócoli (kg)", 3000, 45),
    Producto(24, "Patilla (kg)", 3500, 40),
    Producto(25, "Acelga (kg)", 1800, 75),
    Producto(26, "Yuca (kg)", 2000, 70),
    Producto(27, "Remolacha (kg)", 2200, 65),
    Producto(28, "Apio (kg)", 2400, 60),
    Producto(29, "Pimiento (kg)", 2600, 55),
    Producto(30, "Jengibre (kg)", 2800, 50),
    Producto(31, "Ajo (kg)", 3000, 45),
    Producto(32, "Echalote (kg)", 3200, 40),
    Producto(33, "Champiñones (kg)", 3500, 35),
    Producto(34, "Escarola (kg)", 2000, 60),
    Producto(35, "Puerro (kg)", 1800, 65),
    Producto(36, "Perejil (kg)", 2200, 55),
    Producto(37, "Albahaca (kg)", 2400, 50),
    Producto(38, "Cilantro (kg)", 2600, 45),
    Producto(39, "Romero (kg)", 2800, 40),
    Producto(40, "Orégano (kg)", 3000, 35),
    Producto(41, "Hierbabuena (kg)", 3200, 30),
    Producto(42, "Eneldo (kg)", 3500, 25),
    Producto(43, "Tomillo (kg)", 1800, 60),
    Producto(44, "Mostaza (kg)", 2000, 55),
    Producto(45, "Estragón (kg)", 2200, 50),
    Producto(46, "Canela (kg)", 2400, 45),
    Producto(47, "Clavo (kg)", 2600, 40),
    Producto(48, "Nuez Moscada (kg)", 2800, 35),
    Producto(49, "Cúrcuma (kg)", 3000, 30),
    Producto(50, "Cardamomo (kg)", 3200, 25)
]

# Funcion para obtener el producto por su id
def obtener_producto(id_producto):
    for producto in lista_productos:
        if producto.id == id_producto:
            return producto
    return None

# Funcion que muestra los productos
def mostrar_productos():
    return lista_productos