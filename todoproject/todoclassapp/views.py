from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from todoapp.models import Task
from todoapp.forms import ToDoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

'''class TaskListview(ListView):
    model = Task
    fields='__all__'
    success_url=reverse_lazy('check')

    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context['task']=Task.objects.all()
        return context'''


class TaskListview(ListView):
    model = Task
    template_name = 'index.html'
    form_class=ToDoForm
    context_object_name = 'task'
    '''fields = ('name', 'priority', 'date')
    def get_success_url(self):
        return reverse_lazy('todoclassapp:cbvhome',kwargs={'pk':self.object.id})'''


class TaskDetailview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'

class TaskUpdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('todoclassapp:cbvdetail',kwargs={'pk':self.object.id})

class TaskDeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    #context_object_name = 'task'
    success_url = reverse_lazy('todoclassapp:cbvhome')
