from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import RegisterForm
from .forms import TaskForm
from datetime import date, datetime
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! Please login.")
            return redirect('login')

        else:
            print("FORM ERRORS:", form.errors)   # For debugging

    else:
        form = RegisterForm()

    return render(request, 'tasks/register.html', {'form': form})


@login_required(login_url='login')
def home(request):
    today = date.today()
    tasks = Task.objects.filter(user=request.user)
    context = {
        'tasks': tasks,
        'today': today,
    }
    return render(request, 'tasks/home.html', {'tasks': tasks})

@login_required
def tasks_by_date(request, selected_date):
    date_obj = datetime.strptime(selected_date, "%Y-%m-%d").date()
    tasks = Task.objects.filter(user=request.user, date=date_obj)

    context = {
        'tasks': tasks,
        'selected_date': date_obj,
    }
    return render(request, 'tasks/home.html', context)


@login_required
def create_task(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('tasks:home')
    return render(request, 'tasks/form.html', {'form': form})

@login_required
def update_task(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:home')
    context = {'form': form}
    return render(request, 'tasks/form.html', context)

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
    if request.method == "POST":
        task.delete()
        return redirect('tasks:home')
    return render(request, 'tasks/delete.html', {'task': task})


