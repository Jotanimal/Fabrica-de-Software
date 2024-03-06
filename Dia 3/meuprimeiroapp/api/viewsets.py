from rest_framework_viewsets import ModelViewSet
from ..models import PessoaBancoDeDados
from .serializers import PessoaSerializer

class PessoaViewSet(ModelViewSet):
    serializer_class = PessoaSerializer
    queryset = PessoaBancoDeDados.objects