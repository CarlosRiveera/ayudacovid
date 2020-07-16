from django.urls import path, include
from . import views 

urlpatterns = [

    path('', views.beneficiario_form, name="beneficiario_insert"),
    path('<int:id>/', views.beneficiario_form,name='beneficiario_update'),
    path('delete/<int:id>/',views.beneficiario_delete,name='beneficiario_delete'),
    path('list/', views.beneficiario_list, name="beneficiario_list")
    
]