from django.contrib import admin
from . models import Head, Header, Footer, Campaign, Hero
# Register your models here.

@admin.register(Head, Header,  Footer, Campaign, Hero)
class PostAdmin(admin.ModelAdmin):
    pass
