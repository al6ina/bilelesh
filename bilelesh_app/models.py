from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Reservation(models.Model):
    phone_number = models.BigIntegerField()
    people_count = models.IntegerField()
    place_id = models.ForeignKey(Place, on_delete=models.CASCADE)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.phone_number
