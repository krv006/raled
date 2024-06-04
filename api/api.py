from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

from .serializers import CategorySerializer, ProductSerializer, AboutSerializer
from .serializers import ContactSerializer, WorkerSerializer, Social_mediaSerializer

from .models import Category, Product, Contact, About, Worker, Social_media




class CategoryListCreateAPIView(ListCreateAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()

        name = self.request.query_params.get('name', None)

        if name:
            queryset = queryset.filter(name=name)

        return queryset



class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListCreateAPIView(ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()

        name = self.request.query_params.get('name', None)
        category = self.request.query_params.get('category', None)

        if name:
            queryset = queryset.filter(name=name)
        if category:
            queryset = queryset.filter(category=category)

        return queryset 

class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ContactListCreateAPIView(ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer



class AboutListCreateAPIView(ListCreateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class AboutRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer



class WorkerListCreateAPIView(ListCreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

class WorkerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class Social_mediaListCreateAPIView(ListCreateAPIView):
    queryset = Social_media.objects.all()
    serializer_class = Social_mediaSerializer

class Social_mediaRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Social_media.objects.all()
    serializer_class = Social_mediaSerializer


# class ReconcileListCreateAPIView(ListCreateAPIView):
#     queryset = Reconcile.objects.all()
#     serializer_class = ReconcileSerializer

# class ReconcileRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Reconcile.objects.all()
#     serializer_class = ReconcileSerializer

# class RediktListCreateAPIView(ListCreateAPIView):
#     queryset = Redikt.objects.all()
#     serializer_class = RediktSerializer

# class RediktRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Redikt.objects.all()
#     serializer_class = RediktSerializer
