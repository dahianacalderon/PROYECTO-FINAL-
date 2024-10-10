from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm
from .models import Producto, DetalleCarrito
from django.contrib.auth import get_user

def profile_view(request):
    return render(request, 'profile.html')  

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña inválidos.')
    
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Te has registrado correctamente.')
            return redirect('inicio')
    else:
        register_form = RegisterForm() 

    return render(request, 'register.html', {'register_form': register_form})

def inicio(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contacto(request):
    return render(request, 'contacto.html')

def shop(request):
    productos = Producto.objects.all()
    return render(request, 'shop.html', {'productos': productos})

def car(request):
    car_items = DetalleCarrito.objects.filter(carrito__cliente__user=request.user)  # Cambié DetalleCar a DetalleCarrito
    total = sum(item.subtotal for item in car_items)
    context = {
        'car_items': car_items,
        'total': total,
    }
    return render(request, 'car.html', context)

def salir(request):
    logout(request)
    messages.success(request, "Tu sesión ha sido cerrada correctamente")
    return redirect('inicio')

def buscar(request):
    query = request.GET.get('q')
    resultados = []

    if query:
        resultados = Producto.objects.filter(nombre__icontains=query)

    return render(request, 'resultado_busqueda.html', {'resultado': resultados, 'query': query})

def agregar_al_car(request):
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        producto = get_object_or_404(Producto, id=producto_id)

        # Agregar el producto al carrito
        car_item, created = car.objects.get_or_create(
            user=request.user,
            producto=producto,
        )

        if not created:
            # Si el producto ya existe en el carrito, incrementa la cantidad
            car_item.cantidad += 1
            car_item.save()

        return redirect('productos')

def ver_car(request):
    car_items = car.objects.filter(user=request.user)
    total = sum(item.producto.precio * item.cantidad for item in car_items)
    return render(request, 'car.html', {'car_items': car_items, 'total': total})

def completar_perfil(request):
    # Lógica de la vista
    return render(request, 'completar_perfil.html')

def producto_view(request):
    productos = Producto.objects.all()  # Obtener todos los productos
    return render(request, 'productos.html', {'productos': productos})
