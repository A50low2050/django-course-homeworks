from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    SORT_MAP = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price',
    }

    sort = request.GET.get('sort')
    phones = Phone.objects.all()
    template = 'catalog.html'

    if sort:
        phones = phones.order_by(SORT_MAP[sort])
    context = {'phones': phones}
    return render(request, template, context)

    # if sort == 'name':
    #     phones = Phone.objects.all().order_by('name')
    #     context = {'phones': phones}
    #     return render(request, template, context)
    #
    # if sort == 'min_price':
    #     phones = Phone.objects.all().order_by('price')
    #     context = {'phones': phones}
    #     return render(request, template, context)
    #
    # if sort == 'max_price':
    #     phones = Phone.objects.all().order_by('-price')
    #     context = {'phones': phones}
    #     return render(request, template, context)



def show_product(request, slug):
    phone = Phone.objects.filter(slug=slug).first()
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)
