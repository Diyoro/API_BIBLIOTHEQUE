from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'auteur', 'active', 'created')
    fields = ('nom', 'auteur', 'active')

@admin.register(Livre)
class LivreAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'image', 'auteur', 'document', 'active', 'created')
    fields = ('nom', 'description', 'image', 'auteur', 'document', 'active',)