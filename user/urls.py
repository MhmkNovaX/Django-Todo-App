from django.urls import path

from .views import Login, Logout, Signup

urlpatterns = [
    path('login/', Login.as_view(), name='Login'),
    path('logout/', Logout.as_view(), name='Logout'),
    path('signup/', Signup.as_view(), name='Signup'),
]