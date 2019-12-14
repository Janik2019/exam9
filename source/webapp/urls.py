from django.urls import path
from .views import IndexView, PhotoView, PhotoCreateView


app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('photo/<int:pk>/', PhotoView.as_view(), name='photo_detail'),
    path('products/create/', PhotoCreateView.as_view(), name='photo_create')
]