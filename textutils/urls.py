"""textutils URL Configuration

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
from django.contrib import admin
from django.urls import path
from . import views

# Control will first come to the urls.py and search for the queried path. If nothing is given, index page will open.
# If the url is given with about in the end, about page will open. The control goes to the views.py and searches for the method name given here.
# 'name' attribute is to get this method from anywhere in the project.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('about', views.about, name = 'about'),
    path('contact', views.contact, name = 'contact'),
    # path('removepunc', views.removepunc, name = 'rmvpun'),
    # path('capitalizefirst', views.capfirst, name = 'capfirst'),
    # path('spaceremove', views.spaceremove, name = 'spcrmv'),
    # path('newlineremove', views.newlineremove, name = 'newlnrmv'),
    # path('charcount', views.charcount, name = 'charcount')
    path('analyze', views.analyze, name = 'analyze')
]
