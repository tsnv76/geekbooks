from django.shortcuts import render


def main(request):
    return render(request, 'mainapp/index.html')


def products(request):
    return render(request, 'mainapp/shop-list.html')


def contact(request):
    return render(request, 'mainapp/contact.html')
