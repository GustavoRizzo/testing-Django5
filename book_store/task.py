from django_rq import job


@job
def somar_dois_numeros(a, b):
    resultado = a + b
    return resultado
