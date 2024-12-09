from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Mattle
from .serializer import MattleSerializer


@api_view(['GET', 'POST'])
def mattle_list(request,pk=None):
    if request.method == 'GET':
        id=pk
        if id is not None:
            mattles=Mattle.objects.get(id=id)
            serializer=MattleSerializer(mattles)
            return Response(serializer.data)
        mattles = Mattle.objects.all()
        serializer = MattleSerializer(mattles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        return upload_data(request)


def upload_data(request):
    if request.method == 'POST':
        serializer = MattleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
