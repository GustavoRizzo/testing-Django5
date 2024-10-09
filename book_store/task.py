import time
from celery import shared_task
# from django_rq import job


# @job
# def somar_dois_numeros(a, b):
#     resultado = a + b
#     return resultado


@shared_task
def add(x, y):
    # add delay 30 segundos
    time.sleep(30)
    return x + y
