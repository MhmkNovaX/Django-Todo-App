from django.shortcuts import render
from django.views import View
from django.db.models import Q

from .models import Task

class TaskList(View):
    def get(self, request):
        context = {}
        q = Q()
        if request.GET.get('search'):
            q = q & Q(title__icontains=request.GET.get('search'))
        context['tasks'] = Task.objects.filter(q)
        return render(request, 'task_list.html', context)