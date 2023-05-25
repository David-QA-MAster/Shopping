from django.urls import path
from Site import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre-a-empresa', views.institucional, name='institucional'),
    path('cadastro', views.cadastro_cliente, name='cadastro_cliente'),
    path('contato', views.contato_cliente, name='contato_cliente'),
    path('produtos', views.produto_lista, name='produto_lista'),
    path('produtos/<int:id>', views.produto_lista_por_id, name= 'produto_lista_por_id'),
    path('produto/<int:id>', views.produto_detalhe, name='produto_detalhe'),


]