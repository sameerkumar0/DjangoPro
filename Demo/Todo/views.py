from django.shortcuts import render,redirect,get_object_or_404
from .models import Todo,User
from django.contrib import messages
# Create your views here.


# def todo_list(request):
#     todos = Todo.objects.all()
#     return render(request, "todo_list.html", {"todos": todos})

# def todo_detail(request, pk):
#     todo = get_object_or_404(Todo, pk=pk)
#     return render(request, "todo_detail.html", {"todo": todo})

# #create view
# def todo_create(request):
#     if request.method == "POST":
#         title = request.POST.get("title")
#         description = request.POST.get("description")
#         completed = request.POST.get("completed") == "on"
#         Todo.objects.create(title=title, description=description, completed=completed)
#         return redirect("todo_list")
#     return render(request, "todo_form.html")

# # update view
# def todo_update(request, pk):
#     todo = get_object_or_404(Todo, pk=pk)

#     if request.method == "POST":
#         todo.title = request.POST.get("title")
#         todo.description = request.POST.get("description")
#         todo.completed = request.POST.get("completed") == "on"
#         todo.save()
#         return redirect("todo_list")

#     return render(request, "todo_form.html", {"todo": todo})

# # delete view
# def todo_delete(request, pk):
#     todo = get_object_or_404(Todo, pk=pk)

#     if request.method == "POST":
#         todo.delete()
#         return redirect("todo _list")

#     return render(request, "todo_confirm_delete.html", {"todo": todo})

# class based views

from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Todo

# List all todos
class TodoListView(ListView):
    model = Todo
    template_name = "todo_list.html"
    context_object_name = "todos"

# Show details of a single todo
class TodoDetailView(DetailView):
    model = Todo
    template_name = "todo_detail.html"
    context_object_name = "todo"

# Create a new todo
class TodoCreateView(CreateView):
    model = Todo
    template_name = "todo_form.html"
    fields = ["title", "description", "completed"]
    success_url = reverse_lazy("todo_list")

# Update an existing todo
class TodoUpdateView(UpdateView):
    model = Todo
    template_name = "todo_form.html"
    fields = ["title", "description", "completed"]
    success_url = reverse_lazy("todo_list")

# Delete a todo
class TodoDeleteView(DeleteView):
    model = Todo
    template_name = "todo_confirm_delete.html"
    success_url = reverse_lazy("todo_list")


# user register
def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if user already exists
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'Email already registered'})

        # Create and save user
        user = User(username=username, email=email)
        user.set_password(password)  # Hash password
        user.save()

        return redirect('login')  

    return render(request, 'register.html')

#user login
def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                request.session['user_id'] = user.id  # Store user session
                return redirect('todo_list')
            else:
                messages.error(request, 'Invalid credentials')
        except User.DoesNotExist:
            messages.error(request, 'Invalid credentials')

    return render(request, 'login.html')