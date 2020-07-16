from django.urls import path, include
from . import views 

urlpatterns = [

    path('', views.tipo_ayuda_form, name="tipo_ayuda_insert"),
    path('<int:id>/', views.tipo_ayuda_form,name='tipo_ayuda_update'),
    path('delete/<int:id>/',views.tipo_ayuda_delete,name='tipo_ayuda_delete'),
    path('list/', views.tipo_ayuda_list, name="tipo_ayuda_list")
    
]