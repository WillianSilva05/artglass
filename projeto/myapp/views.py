from django.shortcuts import render, redirect, HttpResponse
from .forms import LoginForm, addVendaForm, editMetaForm
from .models import Usuario, Vendas
from django.db.models import Sum
# Create your views here.


def index(request):
    profile = {}
    profile['form'] = LoginForm()
    return render(request, 'login.html', profile)

def home(request):
    profile = {}
    profile['form'] = LoginForm()
    profile['venda'] = addVendaForm()
    profile['editMeta'] = editMetaForm()
    try:
        profile['uid'] = Usuario.objects.get(id=request.session['uid'])
        profile['log'] = 1
        profile['vendas'] = Vendas.objects.filter(
            id_usuario=request.session['uid']).aggregate(Sum('valor'))
    except KeyError:
        profile['log'] = 0
        return redirect('index')
    return render(request, 'index.html', profile)


def dologin(request):
    if request.method == "POST":
        try:
            u = Usuario.objects.get(usuario=request.POST['usuario'])
        except:
            return HttpResponse("Usuario ou senha inválidos")
        if u.senha == request.POST['senha']:
            request.session['uid'] = u.id
            return redirect('home')
        else:
            return HttpResponse("Usuario ou senha inválidos")
    else:
        return redirect('login')


def logout(request):
    try:
        del request.session['uid']
    except:
        return redirect('index')
    return redirect('index')


def addVenda(request):
    if request.method == 'POST':
        c = Vendas(id_usuario=Usuario.objects.get(
            id=request.session['uid']).id, valor=request.POST['valor'])
        c.save()
    return redirect('home')


def historico(request):
    data = {}
    try:
        data['uid'] = Usuario.objects.get(id=request.session['uid'])
        data['log'] = 1
        data['vendas'] = Vendas.objects.filter(id_usuario=request.session['uid'])
    except KeyError:
        data['log'] = 0
        return redirect('index')
    return render(request, 'historico.html', data)


def deleteVenda(request, id):
    data = {}
    try:
        data['uid'] = Usuario.objects.get(id=request.session['uid'])
        data['log'] = 1
        data['vendas'] = Vendas.objects.filter(id_usuario=request.session['uid'])
        record = Vendas.objects.get(id=id)
        record.delete()
    except KeyError:
        data['log'] = 0
        return redirect('index')
    return render(request, 'historico.html', data)



def editMeta(request):
    if request.method == 'POST':
        userMeta = Usuario.objects.get(id=request.session['uid'])
        userMeta.meta = request.POST['meta']
        userMeta.save()
    return redirect('home')