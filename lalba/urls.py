"""lalba URL Configuration

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
from django.views.generic import TemplateView
from reservations import views as reservation_views
from contact import views as contact_views
from django.conf.urls import handler404
from . import views
from .views import error_404_view

handler404 = error_404_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('about/', TemplateView.as_view(
        template_name='about.html'), name='about'),
    path('menu/', TemplateView.as_view(
        template_name='menu.html'), name='menu'),
    path('accounts/', include('allauth.urls')),
    path('reservations/',
         reservation_views.reservation_list, name='reservation_list'),
    path('reservations/new/',
         reservation_views.new_reservation, name='new_reservation'),
    path('reservations/report/<int:booking_id>/',
         reservation_views.reservation_report, name='reservation_report'),
    path('reservations/update/<int:booking_id>/',
         reservation_views.update_reservation, name='update_reservation'),
    path('reservations/<int:booking_id>/delete/',
         reservation_views.delete_reservation, name='delete_reservation'),
    path('contact/', contact_views.contact_view, name='contact'),

]
