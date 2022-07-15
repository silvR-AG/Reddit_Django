from django.urls import path
from . import views

urlpatterns = [
    # path('matchplayed/', views.matches_per_year),
    path('', views.index)
    
]