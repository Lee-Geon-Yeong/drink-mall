from django.urls import path
from drinks.views import list_view

app_name='drinks'

urlpatterns = [
    path('list/', list_view, name='list_view'),
]