from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . models import Task
from .forms import ToDoForm
'''
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

# Create your views here.
class TaskListview1(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name='task'

class TaskDeleteview1(DeleteView):
    model = Task
    template_name = 'delete.html'
    #context_object_name = 'task'
    success_url = reverse_lazy('cbvhom')
'''


def add(request):
    task = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        task1=Task(name=name,priority=priority,date=date)
        task1.save()
    return render(request,'home.html',{'task':task})

'''def details(request):
    task=Task.objects.all()
    return render(request,'details.html',{'task':task})'''

def delete(request,id):
    if request.method=='POST':
        task=Task.objects.get(id=id)
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)
    f=ToDoForm(request.POST or None,instance=task)
    if f.is_valid():
       f.save()
       return redirect('/')

    return render(request, 'edit.html', {'form': f, 'task': task})

