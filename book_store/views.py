from book_store.task import somar_dois_numeros
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

@api_view(['GET'])
def resultado_tarefa(request, a, b):
    # Chama a tarefa assíncrona para somar dois números
    task_result = somar_dois_numeros.delay(a, b)

    # Retorna uma resposta com o ID da tarefa para que o cliente possa verificar o status posteriormente
    return Response({'task_id': task_result.id})
