from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Memes, Frog
from .serializers import MemesSerializer

# Create your views here.
class GetMemesInfoView(APIView):
    def get(self, request):
        # Извлекаем набор всех записей из таблицы Capital
        queryset = Memes.objects.all()
        # Создаём сериалайзер для извлечённого наборa записей
        serializer_for_queryset = MemesSerializer(
            instance=queryset,  # Передаём набор записей
            many=True  # На вход подается именно набор, а не одна запись
        )
        return Response(serializer_for_queryset.data)

def memes_list(request):
    list_of_memes = Frog.objects.all()
    context = {'list_of_memes': list_of_memes}
    return render(request, 'pepega_in_action/memes_list.html', context)
