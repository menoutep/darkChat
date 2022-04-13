"""studyBud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from django.contrib.auth import views as auth_views
from .import views 
from accounts.forms import LoginForm
app_name='accounts'

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html.twig', redirect_authenticated_user=True, authentication_form=LoginForm), name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name='accounts/logout.html.twig', next_page='accounts:login'), name="logout"),
    path('register/',views.register, name="register")
    
]
