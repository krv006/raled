from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    LANGUAGE_CHOICES = [
        ('uz', 'Uzbek'),
        ('ru', 'Russian'),
        ('en', 'English'),
        # nechta til sorash!
    ]

    name = models.CharField(max_length=250)
    description_uz = models.TextField()
    description_ru = models.TextField()
    description_en = models.TextField()
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default='uz')
    url = models.URLField()
    thumb = models.ImageField(upload_to='thumbs/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    doi = models.CharField(max_length=200, blank=True, null=True)
    best = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Contact(models.Model):
    univercity_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.univercity_name


class About(models.Model):
    address = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    phone_number = models.CharField(max_length=1000)

    def __str__(self):
        return self.address


class Worker(models.Model):
    full_name = models.CharField(max_length=50)
    work = models.CharField(max_length=55)
    image = models.ImageField(upload_to='workers/image')

    def __str__(self):
        return self.full_name


class Social_media(models.Model):
    icon = models.CharField()
    url = models.URLField()


class Partner(models.Model):
    image = models.ImageField(upload_to='thumbs/partners')
    url = models.URLField()

    def __str__(self):
        return self.url


class Redikt(models.Model):
    name = models.CharField(max_length=255)
    work_place_uz = models.TextField()
    work_place_ru = models.TextField()
    work_place_en = models.TextField()
    url_linkedin = models.URLField()

    def __str__(self):
        return self.name
