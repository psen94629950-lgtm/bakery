from django.urls import path
from .views import TeamListCreateView, TeamDetailView

urlpatterns = [
    path('team/', TeamListCreateView.as_view(), name='team-list'),
    path('team/<int:pk>/', TeamDetailView.as_view(), name='team-detail'),
]
