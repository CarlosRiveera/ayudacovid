from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.home, name = "Home"),
    path('', views.ReporteExcel, name = "reporte_excel"),
    path('<int:id>/', views.home,name='detalle'),
    path('admin/', admin.site.urls),
    path('usuario/', include('registro_usuario.urls')),
    path('tipoAyuda/', include('tipo_ayuda.urls')),
    path('entidad/', include('entidad.urls')),
    path('beneficiario/', include('beneficiario.urls')),
    path('ayuda/', include('ayuda.urls')),
    path('detalleAyuda/', include('detalle_ayuda.urls'))
]
