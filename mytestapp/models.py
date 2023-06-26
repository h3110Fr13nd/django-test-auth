from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    # set default time to now
    time = models.IntegerField(default=2)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    def __str__(self):
        return self.name