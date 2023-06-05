from django.shortcuts import render
from Site.forms import ClientesForm, ContatoForms
from Site.models import Departamento, Produto
from django.core.mail import send_mail

# Create your views here.
def index(request):
    produtos_em_destaque= Produto.objects.filter(destaque = True)
    context = {
        'produtos': produtos_em_destaque
    }
    return render(request, 'index.html', context)


def produto_lista(request):
     produtos = Produto.objects.all() 
     context = {
        'produtos': produtos,
        'nome_categoria': "Produtos do 1º Campeão Mundial - 1951 Palmeiras"
    }
     return render(request, 'produtos.html', context) 


def produto_lista_por_id(request, id):
     departamentos= Departamento.objects.all()
     produtos_por_departamento = Produto.objects.filter(departamento_id = id)
     categoria = departamentos.get(id = id).nome

     context = {
        'produtos' : produtos_por_departamento,
        'nome_categoria' : categoria
    }
     return render(request, 'produtos.html', context) 


def produto_detalhe(request, id):
     produto = Produto.objects.get(id = id)
     produtos_relacionados = Produto.objects.filter(departamento_id = produto.departamento.id)[:5]

     context = {
        'produto': produto,
        'produtos_relacionados' : produtos_relacionados
    }
     return render(request, 'produto_detalhes.html', context)


def institucional(request):
     context = {
    }
     return render(request, 'empresa.html', context)


def cadastro_cliente(request):
     mensagem = ''
     # quando envio o formulario preenchido
     if request.method == "POST":
          formulario = ClientesForm(request.POST)
          if formulario.is_valid():
               formulario.save()
               formulario = ClientesForm()
               mensagem = "Cliente Cadastrado com Sucesso"            
     # quando entro n atela vazia

     else:
          formulario = ClientesForm()

     context = {
        'form_cliente' : formulario,
        'mensagem': mensagem
    }
     return render(request, 'cadastro.html', context)


def contato_cliente(request):
     mensagem = ""


     if request.method == "POST":
        nome = request.POST['nome']
        telefone = request.POST['telefone']
        assunto = request.POST['assunto']
        mensagem = request.POST['mensagem']
        remetente = request.POST['email']
        destinatario = ['profronicosta@gmail.com']
        corpo = f"Nome: {nome} \nTelefone: {telefone}  \nMensagem: {mensagem}"
    
        try:
            send_mail(assunto, corpo, remetente, destinatario )
            mensagem = 'E-mail enviado com sucesso!'
        except:
            mensagem = 'Erro ao enviar e-mail!'
     
     formulario = ContatoForms()

     context = {
        'form_contato' : formulario,
        'mensagem' : mensagem
    }

     return render(request, 'contato.html', context)
