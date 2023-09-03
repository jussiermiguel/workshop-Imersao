from rest_framework import serializers
from .models import Aluno

# Definindo um serializer para a classe Aluno
class AlunoSerializer(serializers.ModelSerializer):
    """
    Serializa objetos da classe Aluno.

    permitindo a criação, leitura, atualização e exclusão
    (operações CRUD) de alunos por meio da API REST.
    """
    class Meta:
        model = Aluno
        fields = '__all__'