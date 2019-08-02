from django.db import models
from django_countries.fields import CountryField
from features.models import Feature


class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    feature = models.ForeignKey(Feature, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.feature.name, self.feature.vote_price)
