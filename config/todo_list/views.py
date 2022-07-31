from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login

from .models import Task


class UserLoginView(LoginView):
    template_name = 'todo_list/login.html'
    fields = '__all__'
    redirect_authenticated_user: bool = True
    
    def get_success_url(self) -> str:
        return reverse_lazy('tasks')
    
class UserRegisterView(FormView):
    template_name = 'todo_list/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(UserRegisterView, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(UserRegisterView, self).get(*args, **kwargs)
        
    
    
    
    

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'todo_list/task_list.html'
    context_object_name = 'tasks'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(completed=False).count()
        
        search_input = self.request.GET.get('search') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains=search_input)
        
        context['search_input']=search_input
        return context
    
    
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'todo_list/task_form.html'
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)
    

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'todo_list/task_form.html'
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('tasks')
    
class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'todo_list/task_delete_confirm.html'
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    