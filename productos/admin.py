from django.contrib import admin

# Register your models here.

from .models import Articulo

@admin.register(Articulo)


class AdminProducto(admin.ModelAdmin):
	list_display = ('nombres', 'descripcion', 'categoria', 'precio','imagen','stores')
	list_filter = ('categoria','stores')
	search_fields = ['nombres']