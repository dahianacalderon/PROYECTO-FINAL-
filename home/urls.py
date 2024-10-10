from django.urls import path, include
from django.contrib.auth.views import LoginView
from home.views import *
from .views import buscar
from django.conf import settings
from django.conf.urls.static import static
from .views import ver_car
from . import views
from .views import producto_view

urlpatterns = [
    path('', inicio, name="inicio"),
    path('quienes_somos/', about, name="about"),
    path('contacto/', contacto, name="contacto"),
    path('shop/', shop, name="shop"),
    path('car/', include('car.urls')),  # Manteniendo la ruta para el carrito
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', register, name='register'),
    path('logout/', salir, name='logout'),
    path('buscar/', buscar, name='buscar'),
    path('accounts/profile/', profile_view, name='profile'),  
     path('agregar-al-car/<int:producto_id>/', views.agregar_al_car, name='agregar_al_car'),
    path('car/', ver_car, name='car'),
    path('completar_perfil/', completar_perfil, name='completar_perfil'),
    path('productos/', producto_view, name='productos'),
    path('agregar-al-car/', agregar_al_car, name='agregar_al_car'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
