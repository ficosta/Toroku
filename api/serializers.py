from cadastro.models import Visitante
from rest_framework import serializers


class VisitanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitante
        fields = ('id','nome','documento','tipo','telefone','impresso')
        extra_kwargs = {'nome': {'required': False},'documento': {'required': False}}
