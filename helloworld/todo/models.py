from django.db import models

class Task(models.Model):
	name = models.CharField(max_length=160)
	
	created = models.DateTimeField(auto_now_add=True, null=True)
	modified = models.DateTimeField(auto_now=True, null=True)

	plan = models.TextField(blank=True)
	
	task_email = models.EmailField(max_length=255, blank=True)
	cost = models.FloatField(blank=True, null=True)
	done = models.BooleanField(default=False)
	postponed_cound = models.IntegerField(default=0)
	
	def __str__(self):
		return self.name