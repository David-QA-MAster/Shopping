from django.shortcuts import render
from Site.forms import ClientesForm 
from Site.models import Departamento, Produto

# Create your views here.
def index(request):
    departamentos= Departamento.objects.all()
    produtos_em_destaque= Produto.objects.filter(destaque = True)
    context = {
        'departamentos': departamentos,
        'produtos': produtos_em_destaque
    }
    return render(request, 'index.html', context)


def produto_lista(request):
     departamentos= Departamento.objects.all()
     produtos = Produto.objects.all() 

     context = {
        'departamentos' : departamentos,
        'produtos': produtos,
        'nome_categoria': "Produtos do 1º Campeão Mundial - 1951 Palmeiras"
    }
     return render(request, 'produtos.html', context) 


def produto_lista_por_id(request, id):
     departamentos= Departamento.objects.all()
     produtos_por_departamento = Produto.objects.filter(departamento_id = id)
     categoria = departamentos.get(id = id).nome

     context = {
        'departamentos' : departamentos,
        'produtos' : produtos_por_departamento,
        'nome_categoria' : categoria
    }
     return render(request, 'produtos.html', context) 


def produto_detalhe(request, id):
     departamentos= Departamento.objects.all()
     produto = Produto.objects.get(id = id)
     produtos_relacionados = Produto.objects.filter(departamento_id = produto.departamento.id)[:5]

     context = {
        'departamentos' : departamentos,
        'produto': produto,
        'produtos_relacionados' : produtos_relacionados
    }
     return render(request, 'produto_detalhes.html', context)


def institucional(request):
     departamentos= Departamento.objects.all()
     context = {
        'departamentos' : departamentos
    }
     return render(request, 'empresa.html', context)


def cadastro_cliente(request):
     departamentos= Departamento.objects.all()

     if request.method == "POST":
          formulario = ClientesForm(request.POST)
          if formulario.is_valid():
               cliente = formulario.save()
               formulario = ClientesForm()
     else:
          formulario = ClientesForm()

     context = {
        'departamentos' : departamentos,
        'form_cliente' : formulario
    }
     return render(request, 'cadastro.html', context)


def contato_cliente(request):
     departamentos= Departamento.objects.all()
     context = {
        'departamentos' : departamentos
    }
     return render(request, 'contato.html', context)
