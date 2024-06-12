from django.shortcuts import render
from .models import Product
def index(request):
    return render(request, 'index.html')

def books(request):
    book = Product.objects.all()
    context = {
        'book' : book,
    }
    return render(request, 'books.html', context)

def about_us(request):
    return render(request, 'about_us.html')