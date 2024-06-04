from django.contrib import admin

from api.models import Category, Partner, Product,  About, Contact, Redikt, Worker, Social_media

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(About)
admin.site.register(Worker)
admin.site.register(Contact)
admin.site.register(Social_media)
admin.site.register(Partner)
admin.site.register(Redikt)