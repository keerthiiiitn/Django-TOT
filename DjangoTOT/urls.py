"""DjangoTOT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from djtot import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('about/',views.abouts),
    path('dynamic/<str:name>/',views.dynamicurl),
    path('message/',views.msg),
    path('details/',views.detailsofme),
    path('table/',views.tables),
    path('tabletask/<int:n>/',views.table),
    path('twoparameters/<str:name>/<int:age>/',views.twodynamicparameters),
    path('signup/',views.signuppage),
    path('inline/',views.sample),
    path('login/',views.loginpage),
    path('registration/',views.registrationpage),
]
