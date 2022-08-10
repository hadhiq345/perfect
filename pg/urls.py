from django.urls import path
from pg.views import index,rooms_list_cheyyuka

urlpatterns = [
    path('', index),
    path('rooms', rooms_list_cheyyuka),
]
