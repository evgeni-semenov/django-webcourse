from django.db import models

class Task(models.Model):
    taskname = models.CharField(max_length=300)

    def __str__(self):
        return self.taskname