from django.db import models

class DrinkType(models.Model):
    type_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.type_name
        
class Drink(models.Model):
    name = models.CharField(max_length=160)
    type_name = models.ForeignKey(DrinkType, on_delete=models.CASCADE, related_name="drinks")
    alcohol_content = models.IntegerField(default=0)

    def __str__(self):
        return self.name
