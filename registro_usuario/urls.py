from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', include('registro_usuario.urls'))
]
