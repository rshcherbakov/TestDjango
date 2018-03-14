from django.db import models
from django.db.models.deletion import CASCADE
from datetime import datetime as dt
class RatesToStore(models.Model):
    name = models.CharField(max_length=150)

class ExchangeRates(models.Model):
    rate = models.FloatField()
    time = models.DateTimeField()
    currencyid = models.ForeignKey(RatesToStore, on_delete=CASCADE)

    def create(self, rate, currencyId):
        return self.create(rate=rate, currencyid=currencyId, time= dt.now())