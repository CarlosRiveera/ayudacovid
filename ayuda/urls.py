from django.urls import path, include
from . import views 

urlpatterns = [

    path('', views.ayuda_form, name="ayuda_insert"),
    path('<int:id>/', views.ayuda_form,name='ayuda_update'),
    path('delete/<int:id>/',views.ayuda_delete,name='ayuda_delete'),
    path('list/', views.ayuda_list, name="ayuda_list")
    
]