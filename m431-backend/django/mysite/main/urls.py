from django.urls import path

from main import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('appreciations', views.AppreciationList.as_view()),
    path('observation', views.ObservationList.as_view()),
    path('appreciations/<int:pk>', views.AppreciationDetail.as_view()),
    path('observation/<int:pk>', views.ObservationDetail.as_view()),
    
    path('api-token-auth/', obtain_jwt_token),

    path('api-token-verify/', verify_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),


]