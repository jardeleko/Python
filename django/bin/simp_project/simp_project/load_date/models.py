from django.db import models
class CourseManager(models.Manager):
	def search(self, query):
		return self.get_queryset().filter(models.Q(name__icontains=query or
			models.Q(description__icontains=query))
	)
# Create your models here.
class Course(models.Model):
	"""docstring for ClassName"""
	name = models.CharField('Nome', max_length=100)
	slug = models.SlugField('Atalho')
	description = models.TextField('Descrição', blank=True)
	start_date = models.DateField('Data de inicio', null=True, blank=True

	)
	image = models.ImageField(
			upload_to= 'load_date/images', 
			verbose_name='Imagem', null=True, blank=True
	)
	create_at = models.DateTimeField(
		'Criado em', auto_now_add=True 
	)
	update_at = models.DateTimeField('Atualizado em', auto_now=True)
	
	#never sad my line for universite 
	objects = CourseManager()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Curso'
		verbose_name_plural = 'Cursos'
		ordering = ['-name']
