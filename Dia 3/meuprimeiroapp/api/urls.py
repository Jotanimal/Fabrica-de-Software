from rest_framework.router import DefaultRouter
from .viewsets import PessoaViewSet
from django.urls import include

router = DefaultRouter()

router.register("Pessoa", PessoaViewSet)

urlpatterns = [
    path("admin/" "api/", include(router.urls))
    path("", include ("meuprimeiroapp.api.urls"))
]