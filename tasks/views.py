from django.shortcuts import render,redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
# Create your views here.
def index(request):
    data = Task.objects.all()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task-index')
    else:
        form = TaskForm()
    return render(request,"tasks/index.html", {
        "todos" : data,
        "form": form
    })
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = TaskForm(instance=task)
    return render(request, 'tasks/index.html', {'form': form})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task-index')
    return render(request, 'tasks/index.html', {'form': TaskForm(instance=task)})