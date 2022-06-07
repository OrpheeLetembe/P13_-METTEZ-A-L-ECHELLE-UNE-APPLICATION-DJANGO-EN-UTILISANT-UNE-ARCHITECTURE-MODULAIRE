from django.urls import path

from . views import profiles_index, profile, index


urlpatterns = [
    path('', index, name='index'),
    path('profiles/', profiles_index, name='profiles_index'),
    path('profiles/<str:username>/', profile, name='profile'),

]
