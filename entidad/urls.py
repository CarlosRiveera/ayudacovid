from django.urls import path, include
from . import views 

urlpatterns = [

    path('', views.entidad_form, name="entidad_insert"),
    path('<int:id>/', views.entidad_form,name='entidad_update'),
    path('delete/<int:id>/',views.entidad_delete,name='entidad_delete'),
    path('list/', views.entidad_list, name="entidad_list")
    
]