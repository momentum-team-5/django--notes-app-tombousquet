"""notesapp URL Configuration

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
from notes import views as notes_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', notes_views.contact_us, name='contact_us'),
    path('', notes_views.notes_list, name="notes_list"),
    path('<int:pk>/', notes_views.notes_detail, name="notes_detail"),
    path('add/', notes_views.notes_add, name="notes_add"),
    path('delete/<int:pk>/', notes_views.notes_delete, name='notes_delete'),
    path('edit/<int:pk>/', notes_views.notes_edit, name='notes_edit'),
]
