"""
URL configuration for hello project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, re_path
from django.conf import settings
from django.conf.urls.static import static
from firstapp import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('create/', views.create),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('my_form/', views.my_form, name='my_form'),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete),
    path('my_form/delete/<int:id>/', views.delete),
    path('form_up_img/', views.form_up_img, name='form_up_img'),
    path('form_up_img/delete_img/<int:id>/', views.delete_img),
    path('form_up_pdf/', views.form_up_pdf, name='form_up_pdf'), 
    path('form_up_pdf/delete_pdf/<int:id>/', views.delete_pdf), 
    path('form_up_video/', views.form_up_video, name='form_up_video'), 
    path('form_up_video/delete_video/<int:id>/', views.delete_video), 
    path('form_up_audio/', views.form_up_audio, name='form_up_audio'), 
    path('form_up_audio/delete_audio/<int:id>/', views.delete_audio), 
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)










