"""webplayground URL Configuration

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
from django.urls import path, include
from pages.urls import page_patterns

# Lo hacemos asi sin incluir page_patterns
# urlpatterns = [
#     path('', include('core.urls')),
#     path('pages/', include('pages.urls')),
#     path('admin/', admin.site.urls),
# ]

urlpatterns = [
    path('', include('core.urls')),
    path('pages/', include(page_patterns)),
    path('admin/', admin.site.urls),
    # path del Auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
]
