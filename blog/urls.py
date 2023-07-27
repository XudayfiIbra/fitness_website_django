from django.urls import path
from . import views
urlpatterns = [
    path('', views.homePage, name='home'),
    path('categories', views.CategoryViewList, name='category')
]
