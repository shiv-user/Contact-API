from django.db import models

# Create your models here.
class contact(models.Model):
	name = models.CharField(max_length=100, null=False)
	number = models.CharField(max_length=10)
	email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
	spam   = models.BooleanField(default=False)


	def __str__(self):
		return self.number




