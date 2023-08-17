from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import BaseRegisterView
from .views import upgrade_me
from django.contrib import admin
from django.urls import path, include
from django.urls import path
from .views import IndexView

urlpatterns = [
    path('login/',
         LoginView.as_view(template_name = 'sign/login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name = 'sign/logout.html'),
         name='logout'),
    path('signup/',
         BaseRegisterView.as_view(template_name = 'sign/signup.html'),
         name='signup'),
    path('upgrade/', upgrade_me, name='upgrade')
    path('admin/', admin.site.urls),
    path('appointments/', include(('appointment.urls', 'appointments'), namespace='appointments')),
    path('accounts/', include('allauth.urls'),
    path('', IndexView.as_view()),
]