from rest_framework_serializers import ModelSerializer
from ..models import PessoaBancoDeDados

class PessoaSerializer(ModelSerializer):
    class Meta: 
        model = PessoaBancoDeDados
        fields = ["id", "primeiro_nome", "segundo_nome", "idade"]
        