from django.urls import path
from .views import index, Detail, additem, updateitem, deleteitem

app_name = "myapp"

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/', Detail, name ='detail'),
    path('additem/', additem, name ='additem'),
    path('updateitem/<int:id>/', updateitem, name ='updateitem'),
    path('deleteitem/<int:id>/', deleteitem, name ='deleteitem'),

]