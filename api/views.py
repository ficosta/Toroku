from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from cadastro.models import Visitante
from rest_framework import generics
from api.serializers import VisitanteSerializer

@api_view(['GET'])
def Print(request):
    queryset = Visitante.objects.filter(impresso=False)
    serializer = VisitanteSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET','PUT'])
def PrintVisitante(request, pk):
    """
    Retrieve, update or delete a person instance.
    """
    try:
        visitante = Visitante.objects.get(pk=pk)
    except Visitante.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VisitanteSerializer(visitante)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VisitanteSerializer(visitante, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
