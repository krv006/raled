from django.urls import path
from . import views
from django.urls import path
from .api import (
    CategoryListCreateAPIView,
    CategoryRetrieveUpdateDestroyAPIView,
    ProductListCreateAPIView,
    ProductRetrieveUpdateDestroyAPIView,
    ContactListCreateAPIView, 
    ContactRetrieveUpdateDestroyAPIView, 
    AboutListCreateAPIView, 
    AboutRetrieveUpdateDestroyAPIView, 
    WorkerListCreateAPIView, 
    WorkerRetrieveUpdateDestroyAPIView, 
    Social_mediaListCreateAPIView, 
    Social_mediaRetrieveUpdateDestroyAPIView, 
    # ReconcileListCreateAPIView,
    # ReconcileRetrieveUpdateDestroyAPIView,
    # RediktListCreateAPIView,
    # RediktRetrieveUpdateDestroyAPIView,
)
from .views import *

urlpatterns = [
    path('api/categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('api/categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-retrieve-update-destroy'),
    path('api/products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('api/products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-retrieve-update-destroy'),
    path('api/contacts/', ContactListCreateAPIView.as_view(), name='contact-list-create'),
    path('api/contacts/<int:pk>/', ContactRetrieveUpdateDestroyAPIView.as_view(), name='contact-detail'),
    path('api/aboutus/', AboutListCreateAPIView.as_view(), name='aboutus-list-create'),
    path('api/aboutus/<int:pk>/', AboutRetrieveUpdateDestroyAPIView.as_view(), name='aboutus-detail'),
    path('api/workers/', WorkerListCreateAPIView.as_view(), name='worker-list-create'),
    path('api/workers/<int:pk>/', WorkerRetrieveUpdateDestroyAPIView.as_view(), name='worker-detail'),
    path('api/social_media/', Social_mediaListCreateAPIView.as_view(), name='social_media_list_create'),
    path('api/social_media/<int:pk>/', Social_mediaRetrieveUpdateDestroyAPIView.as_view(), name='social_media_detail'), 
    # path('reconcile/', ReconcileListCreateAPIView.as_view(), name='reconcile-list-create'),
    # path('reconcile/<int:pk>/', ReconcileRetrieveUpdateDestroyAPIView.as_view(), name='reconcile-retrieve-update-destroy'),
    # path('redikt/', RediktListCreateAPIView.as_view(), name='redikt-list-create'),
    # path('redikt/<int:pk>/', RediktRetrieveUpdateDestroyAPIView.as_view(), name='redikt-retrieve-update-destroy'),



    path('', index,name='index'),
    path('about_us/', about_us,name='about_us'),
    path('contact/', contact,name='contact'),
    path('books/', books,name='books'),
    path('books/<int:book_id>', book_detail,name='book_detail'),
    path('redikt/', redikt,name='redikt'),
    path('send/', send,name='send'),

]
