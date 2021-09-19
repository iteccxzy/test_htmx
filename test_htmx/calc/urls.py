from django.urls import path
from calc import views


urlpatterns = [
    path('contact', views.contact),
    path('edit', views.edit),
    path('load', views.load),
    path('delete-row', views.delete_row),
    path('lazy', views.lazy),
    path('search', views.search),    
]
