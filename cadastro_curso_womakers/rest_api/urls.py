from django.urls import path
from rest_api.views import hello_world
from rest_framework.routers import SimpleRouter
from rest_api.views import CursoModelViewSet

app_name = 'rest_api'
router = SimpleRouter(trailing_slash=False) #trailing_slash= False significa se vai ou não a barra no final da rota
router.register('curso', CursoModelViewSet)

urlpatterns = [
    path('hello_world', hello_world, name='hello_world_api')
]

urlpatterns += router.urls #concatenação
