from django.contrib import admin
from django.contrib.auth.models import User
from home.models import *

# Register your models here.
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Inventario)
admin.site.register(Opinion)
admin.site.register(Pedido)
admin.site.register(DetallePedido)
admin.site.register(MetodoPago)
admin.site.register(Car)
admin.site.register(DetalleCarrito)

