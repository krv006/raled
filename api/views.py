from django.shortcuts import render
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from .models import Reconcile, Redikt
# from .serializers import ReconcileSerializer, RediktSerializer

from django.core.paginator import Paginator
from api.models import About, Partner, Product, Redikt

def index(request):
    best_books = Product.objects.filter(best=True)
    partner = Partner.objects.all()
    context = {
        'best_books': best_books,
        'partner': partner,
    }
    return render(request, 'index.html', context)

def books(request):
    book_list = Product.objects.all()
    paginator = Paginator(book_list, 7) 
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'book' : book_list,
        'paginator' : paginator,
        'page_number' : page_number,
        'page_obj' : page_obj,
    }
    return render(request, 'books.html', context)

def about_us(request):
    return render(request, 'about_us.html')

def book_detail(request,book_id):
    book = Product.objects.get(id=book_id)
    return render(request, 'book_detail.html',{'book':book})

def detail(request):
    return render (request,'detail.html',{'detail':detail})

def contact(request):
    contact = About.objects.all()
    return render(request, 'contact.html', {'contact':contact})


def redikt(request):
    redikts = Redikt.objects.all()
    return render(request, 'redikt.html',{'redikts':redikts})

def send(request):
    return render(request, 'send.html')