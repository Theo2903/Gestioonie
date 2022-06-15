from django.urls import path

from crud import views

app_name = 'crud'

urlpatterns = [
    path('', views.object_list, name='object_list'),
    path('new', views.object_create, name='object_new'),
    path('edit/<int:pk>', views.object_update, name='object_edit'),
    path('delete/<int:pk>', views.object_delete, name='object_delete'),
]