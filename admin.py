from django.contrib import admin
from . models import Head, Footer, Sidebar, Campaign, Hero
# Register your models here.

@admin.register(Head, Footer, Sidebar, Campaign, Hero)
class PostAdmin(admin.ModelAdmin):
    pass
