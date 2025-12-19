from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Team_d
from .serializers import TeamSerializer

from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class TeamListCreateView(ListCreateAPIView):
    queryset = Team_d.objects.all()
    serializer_class = TeamSerializer


class TeamDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Team_d.objects.all()
    serializer_class = TeamSerializer
