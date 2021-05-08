from django.db import models

class EmailStats(models.Model):
    all_time = models.IntegerField(default=0)
    monthly = models.IntegerField(default=0)
    weekly = models.IntegerField(default=0)
    daily = models.IntegerField(default=0)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)  # cents

    def __str__(self):
        return self.name

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)