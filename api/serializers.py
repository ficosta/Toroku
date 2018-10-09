from cadastro.models import Visitante
from rest_framework import serializers


class VisitanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitante
        fields = '__all__'
