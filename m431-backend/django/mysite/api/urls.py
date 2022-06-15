from django.urls import path

urlpatterns = [
    # path('', views.home, name='home'),
    path('users/', views.user_list),
]