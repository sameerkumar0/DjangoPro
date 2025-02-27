
from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home,name="Home"),
    path('create/',views.create,name='create'),
    path('registration/',views.registration,name="registration"),
    path('read',views.read)

]
