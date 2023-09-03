from rest_framework import serializers
from .models import ConsultaNutricionista

class NutricionistaSerializer(serializers.ModelSerializer):
    """
    Serializa objetos do modelo ConsultaNutricionista.

    O serializer inclui todos os campos do modelo ConsultaNutricionista.
    """
    class Meta:
        model = ConsultaNutricionista
        fields = '__all__'