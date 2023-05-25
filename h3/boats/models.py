from django.db import models

class Boat(models.Model):
    name = models.CharField(max_length=150)
    make = models.CharField(max_length=150)
    engine_hp = models.FloatField(blank=True, null=True)
    owner_name = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    booking_date = models.DateField()
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE)
    lessor_name = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.booking_date}: {self.boat}" 
