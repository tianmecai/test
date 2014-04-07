from django.http import HttpResponse
import datetime

def time(req,dt=0):
    now = datetime.datetime.now();
    return HttpResponse(now + datetime.timedelta(hours=int(dt)))