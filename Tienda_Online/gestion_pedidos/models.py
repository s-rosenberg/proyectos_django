from django.db import models

# no vamos a tener que insertar nada de SQL, lo va a hacer todo django

class Clientes(models.Model):
    nombre = models.CharField(max_length = 30)
    direccion = models.CharField(max_length = 50)
    email = models.EmailField()
    telefono = models.CharField(max_length = 7)

class Articulos(models.Model):
    nombre = models.CharField(max_length = 30)
    seccion = models.CharField(max_length = 30)
    precio = models.IntegerField()

    def __str__(self):
        return f'Nombre: {self.nombre} , Sección: {self.seccion}, Precio: {self.precio}'

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado =  models.BooleanField()
