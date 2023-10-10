from django.urls import path
from .views import index, Contacts, Detail

app_name = "myapp"

urlpatterns = [
    path('', index),
    path('<int:id>/', Detail, name ='detail'),

]