# from re import I
from django.urls import path
from .views import RegisterAPIView,LoginAPIView,LogoutView


# # sc
urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(), name='logout'),
    # path('', ),
    
]