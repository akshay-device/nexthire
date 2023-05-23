from django.urls import path
from . import views

try:
    urlpatterns = [
        path('api/<str:name>/',views.search_amazon),
    ]
except Exception as e:
    print(e)