
from django.urls import path
from . import views
# from .views import TodoListView, TodoDetailView, TodoCreateView, TodoUpdateView, TodoDeleteView
urlpatterns = [
    path("todo_list/", views.todo_list, name="todo_list"),
    path("todo/<int:pk>/", views.todo_detail, name="todo_detail"),
    path("todo/new/", views.todo_create, name="todo_create"),
    path("todo/<int:pk>/edit/", views.todo_update, name="todo_update"),
    path("todo/<int:pk>/delete/", views.todo_delete, name="todo_delete"),

    # path("todo_list", TodoListView.as_view(), name="todo_list"),
    # path("todo/<int:pk>/", TodoDetailView.as_view(), name="todo_detail"),
    # path("todo/new/", TodoCreateView.as_view(), name="todo_create"),
    # path("todo/<int:pk>/edit/", TodoUpdateView.as_view(), name=list/", views.todo_list, name="todo_list/", views.todo_list, name="todo_"todo_update"),
    # path("todo/<int:pk>/delete/", TodoDeleteView.as_view(), name="todo_delete"),
    # user registration and login
    path('',views.user_register,name='register'),
    path('login/',views.user_login,name='login'),

]
