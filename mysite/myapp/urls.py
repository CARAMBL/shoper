from django.urls import path
from .views import index, Detail

app_name = "myapp"

urlpatterns = [
    path('', index),
    path('<int:id>/', Detail, name ='detail'),

]