from django.db import models

# Create your models here.

class Articulo(models.Model):
	nombres = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=100)
	categoria = models.CharField(max_length=100)
	stores = models.CharField(max_length=50)
	precio = models.DecimalField(max_digits=6, decimal_places=2)
	imagen = models.ImageField(blank=True)

	def __str__(self):
		return self.nombres