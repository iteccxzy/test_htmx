from django.urls import path
from calc import views


urlpatterns = [
    path('contact', views.contact),
    path('edit', views.edit),
]
