from django.shortcuts import render
from djutils.decorators import async
from .models import RatesToStore, ExchangeRates
import schedule
import time

@async
def loadData():
    time.time(10)
    names = RatesToStore.objects.name
    print(names)
    print("works")


def initTask():
    print("and here")
    schedule.every(10).second.do(loadData)

print("works here")
initTask()
