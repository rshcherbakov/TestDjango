from __future__ import absolute_import
#from celery.schedules import crontab
from celery.task import periodic_task
from celery.utils.log import get_task_logger

from .models import *
# import pandas_datareader.data as web
import requests
import re

@periodic_task(run_every=5)
def tasks():
    url = 'http://markets.money.cnn.com/common/modules/iframe/currencyConverter.asp'
    symvolWithId = RatesToStore.objects.values_list('name',"id")
    symbols = map(lambda r: re.split('[^\w]',symvolWithId[0]),symvolWithId)
    for symbol in symbols:
        if len(symbols) > 1:
           resp = requests.post(url,{
               "..requester..":"ContentBuffer",
               "convert":"1",
               "amount":"1",
               "base":symbols[0],
               "quote":symbols[1]})
           rate = float(re.sub("([[^(\d|\.)]])","",resp.text))
           ExchangeRates.create(rate,symvolWithId[1])




