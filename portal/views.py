from django.shortcuts import render

def home(request):
    # O Django vai procurar automaticamente na pasta templates/portal/home.html
    return render(request, 'portal/home.html')
def especies(request):
    return render(request, 'portal/especies.html')
def mapa(request):
    return render(request, 'portal/mapa.html')
def dados(request):
    return render(request, 'portal/dados.html')

