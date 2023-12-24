from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, resultado_tarefa

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
urlpatterns = router.urls

urlpatterns += [
    path('resultado-tarefa/<int:a>/<int:b>/', resultado_tarefa, name='resultado_tarefa'),
]
