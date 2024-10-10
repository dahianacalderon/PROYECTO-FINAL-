from django.db import models
from django.contrib.auth.models import User

# Modelo para Clientes
class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=120)
    pais = models.CharField(max_length=45)
    codigo_postal = models.CharField(max_length=45)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} {self.apellido}"

# Modelo para Categorías
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=45)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

# Modelo para Productos
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=45)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    img = models.ImageField(upload_to="producto")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

# Modelo para Inventario
class Inventario(models.Model):
    cantidad_entrada = models.IntegerField()
    cantidad_salida = models.IntegerField()
    fecha_movimiento = models.DateField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

# Modelo para Opiniones
class Opinion(models.Model):
    calificacion = models.DecimalField(max_digits=3, decimal_places=1)
    comentario = models.TextField()
    fecha_opiniones = models.DateTimeField(auto_now_add=True)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)  # Usando cadena

    def __str__(self):
        return f"Opinion de {self.producto.nombre}"

# Modelo para Pedidos
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    metodo_pago = models.ForeignKey('MetodoPago', on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pedido {self.id}"

# Modelo para Detalle de Pedidos
class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detalle {self.pedido.id} - {self.producto.nombre}"

# Modelo para Métodos de Pago
class MetodoPago(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

# Modelo para Carritos
class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.producto.nombre} - {self.cantidad}"

# Modelo para Detalle de Carritos
class DetalleCarrito(models.Model):
    carrito = models.ForeignKey(Car, on_delete=models.CASCADE)  # Cambiado a Car
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Carrito {self.carrito.id} - {self.producto.nombre}"
