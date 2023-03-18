from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task


class TaskList(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        context = {}
        q = Q(deleted=False)
        if request.GET.get('search'):
            q = q & Q(title__icontains=request.GET.get('search'))
        context['tasks'] = Task.objects.filter(q)
        return render(request, 'task_list.html', context)


class TaskDetail(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, pk):
        context = {}
        try:
            task = Task.objects.get(id=pk)
            context['task'] = task
        except:
            return redirect('NotFound')
        return render(request, 'task_detail.html', context)

    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        if request.POST.get('delete'):
            task.delete()
        else:
            task.title = request.POST.get('title', task.title)
            task.detail = request.POST.get('detail', task.detail)
            task.completed = request.POST.get('completed', task.completed)
            task.save()
        return redirect('TaskList')


class TaskCreate(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        return render(request, 'task_create.html', {})

    def post(self, request):
        task = Task(title=request.POST.get('title'),
                    detail=request.POST.get('detail'),
                    owner=request.user)
        task.save()
        return redirect('TaskList')
