from django.urls import path
from Site import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre-a-empresa', views.institucional, name='institucional'),
    path('cadastro', views.cadastro_cliente, name='cadastro_cliente'),
    path('contato', views.contato_cliente, name='contato_cliente'),
    path('produtos', views.produto_lista, name='produto_lista'),
    path('produto', views.produto_lista, name='produto_detalhe'),


]