from django.db import models

TIPODISCO = ((1,'CD'),
			 (2,'DVD'),)

CATDISCO = ((1,'ANIMES'),
			(2,'CURSOS'),
			(3,'DORAMAS'),
			(4,'ENCICLOPEDIAS'),
			(5,'JUEGOS INFANTILES'),
			(6,'JUEGOS PC'),
			(7,'JUEGOS WII'),
			(8,'MANUALES'),
			(9,'PROGRAMAS MAC'),
			(10,'PROGRAMAS PC'),)


class Disco(models.Model):
	clave = models.CharField(max_length=10, primary_key=True)
	nombre = models.CharField(max_length=255)
	cantdiscos = models.IntegerField(default=1)
	tipodisco = models.IntegerField(choices=TIPODISCO)
	categoria = models.IntegerField(choices=CATDISCO)
	stock = models.IntegerField(default=1)
	existencia = models.IntegerField(default=0)

	class Meta:
		verbose_name = 'Disco'
		verbose_name_plural = 'Discos'
		ordering = ('categoria', 'nombre',)

	def __str__(self):
		return self.nombre

	def __unicode__(self):
		return self.nombre
