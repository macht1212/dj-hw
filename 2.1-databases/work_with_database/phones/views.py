from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', None)
    match sort:
        case 'name':
            phones = Phone.objects.order_by('name')
        case 'min_price':
            phones = Phone.objects.order_by('price')
        case 'max_price':
            phones = Phone.objects.order_by('-price')
        case _:
            phones = Phone.objects.all()
    context = {'phones': phones}
    
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
