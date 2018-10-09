from cadastro.models import Visitante
from rest_framework import generics
from api.serializers import VisitanteSerializer


class PrintViewSet(generics.ListAPIView):
    queryset = Visitante.objects.all()
    serializer_class = VisitanteSerializer
