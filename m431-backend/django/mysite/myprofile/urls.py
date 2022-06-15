from django.urls import path

from myprofile import views

app_name = 'myprofile'

urlpatterns = [
    path('edit/', views.edit, name='edit'),
    path('', views.profile, name='detail'),
    path('user', views.UserList.as_view()),
    path('user/<int:pk>', views.UserDetail.as_view())
]
