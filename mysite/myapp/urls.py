from django.urls import path
from .views import additem, updateitem, deleteitem, ProductListView, ProductDetail, ProductDeleteView

app_name = "myapp"

urlpatterns = [
    # path('', index, name='index'),
    path('', ProductListView.as_view(), name='index'),
    path('<int:pk>/', ProductDetail.as_view(), name ='detail'),
    path('additem/', additem, name ='additem'),
    path('updateitem/<int:id>/', updateitem, name ='updateitem'),
    path('deleteitem/<int:pk>/', ProductDeleteView.as_view(), name ='deleteitem'),

]