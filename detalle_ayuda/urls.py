from django.urls import path, include
from . import views 

urlpatterns = [

    path('', views.detalle_ayuda_form, name="detalle_ayuda_insert"),
    path('<int:id>/', views.detalle_ayuda_form,name='detalle_ayuda_update'),
    path('delete/<int:id>/',views.detalle_ayuda_delete,name='detalle_ayuda_delete'),
    path('list/', views.detalle_ayuda_list, name="detalle_ayuda_list")
    
]