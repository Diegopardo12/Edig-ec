from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='batman.png')

	def __str__(self):
		return f'Perfil de {self.user.username}'

	def following(self):
		user_ids = Relationship.objects.filter(from_user=self.user)\
								.values_list('to_user_id', flat=True)
		return User.objects.filter(id__in=user_ids)

	def followers(self):
		user_ids = Relationship.objects.filter(to_user=self.user)\
								.values_list('from_user_id', flat=True)
		return User.objects.filter(id__in=user_ids)


class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
	timestamp = models.DateTimeField(default=timezone.now)
	content = models.TextField()

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return f'{self.user.username}: {self.content}'


class Relationship(models.Model):
	from_user = models.ForeignKey(User, related_name='relationships', on_delete=models.CASCADE)
	to_user = models.ForeignKey(User, related_name='related_to', on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.from_user} to {self.to_user}'

	class Meta:
		indexes = [
		models.Index(fields=['from_user', 'to_user',]),
		]

class Estudiante(models.Model):
    
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=20)
    edad = models.IntegerField()
    cedula = models.IntegerField()
    correo = models.EmailField(max_length=50)
    celular = models.IntegerField()
    lectivo

    

    def __str__(self):
        return "%s %s %d %d %s %d %s" % (self.nombres, 
                self.apellidos,
                self.edad,
                self.cedula,
                self.correo,
                self.celular,
                self.)
                
class Instructor(models.Model):
    
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    anios_servi = models.IntegerField()
    biogrfia = models.CharField(max_length=200)

    def __str__(self):
        return "%s %s %d %s" % (self.nombre, 
                self.apellidos,
                self.anios_servi,
                self.biogrfia)


class Cursos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    duracion = models.CharField(max_length=100)
    instructor = models.ForeignKey(Instructor,on_delete=models.CASCADE,
                related_name="cursos")

    def __str__(self):
        return "%s %s %s" % (self.nombre, 
                self.descripcion,
                self.duracion)









