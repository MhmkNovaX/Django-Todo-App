from django.shortcuts import render
from django.views import View

class NotFound(View):
    def get(self, request):
        return render(request, '404.html', {})