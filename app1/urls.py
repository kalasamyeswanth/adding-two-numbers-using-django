from django.urls import path
from . import views
urlpatterns = [
    path('',views.happy,name='happy'),
    path('add',views.add,name='add'),
]