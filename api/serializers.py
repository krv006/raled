from rest_framework import serializers
from .models import Category, Product, About, Worker, Contact, Social_media


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name']


class ProductSerializer(serializers.ModelSerializer):

    category = serializers.SerializerMethodField()

    def get_category(self,obj):
        return obj.category.name
    
    class Meta:
        model = Product
        fields = ['id','name', 'description', 'language', 'url', 'thumb', 'category', 'date']

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['id','univercity_name', 'phone_number', 'location']


class AboutSerializer(serializers.ModelSerializer):

    class Meta:
        model = About
        fields = ['id','our_history', 'our_mission', 'fup_regulation']


class WorkerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Worker
        fields = ['id','full_name', 'work', 'image']


class Social_mediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social_media
        fields = ['id','facebook', 'instagram', 'telegram', 'you_tube']

# class ReconcileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Reconcile
#         fields = ['file']

# class RediktSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Redikt
#         fields = ['name', 'work_place', 'discription']