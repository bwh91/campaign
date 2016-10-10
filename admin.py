from django.contrib import admin
from . models import Header, Footer, Sidebar, Campaign, Hero
# Register your models here.

@admin.register(Header, Footer, Sidebar, Campaign, Hero)
class PostAdmin(admin.ModelAdmin):
    pass
