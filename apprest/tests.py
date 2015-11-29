from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Libro, Autor
from .views import *

class PruebasRESTTests(APITestCase):
	def test_mostrar_autor(self):
		a1=Autor(nombre="Juan", apellido = "Martinez")
		a1.save()
		a2=Autor(nombre = "Paco", apellido = "Blanco")
		a2.save()
		response = self.client.get("/autor/")
		self.assertEqual(response.content, '[{"id":1,"nombre":"Juan","apellido":"Martinez"},{"id":2,"nombre":"Paco","apellido":"Blanco"}]')
		print ("VISTA EXITSA")
	def test_crear_libro(self):
		data ={"nombre":"sinsajo", "editorial":"salvat", "genero": "accion"}
		response = self.client.post("/libro/", data, format="json")
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		print("LIBRO CREADO")
