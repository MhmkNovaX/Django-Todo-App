from django.contrib import admin
from django.urls import path, include

from .views import NotFound

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('todo.urls')),
    path('', include('user.urls')),
    path('404/', NotFound.as_view(), name='NotFound')
]
