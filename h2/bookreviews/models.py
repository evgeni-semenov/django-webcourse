from django.db import models

class BookReview(models.Model):
    name = models.CharField(max_length=160)
    review = models.CharField(max_length=600)

    def __str__(self):
        return self.name
