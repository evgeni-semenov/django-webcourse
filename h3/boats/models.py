from django.db import models

class Boat(models.Model):
    name = models.CharField(max_length=150)
    make = models.CharField(max_length=150)
    engine_hp = models.FloatField(blank=True, null=True)
    owner_name = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
