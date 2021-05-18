from django.urls import path
from .views import ( 
    UsersListApiView,
    UserCreateApiView,
    UserRetrieveUpdateDeleteApiView,
    ProfileRetrieveUpdateDeleteApiView
)

app_name = 'users'

urlpatterns = [
    path('', UsersListApiView.as_view(), name='list'),
    path('create/', UserCreateApiView.as_view(), name='create'),
    path('user/', UserRetrieveUpdateDeleteApiView.as_view(), name='user'),
    path('profile/', ProfileRetrieveUpdateDeleteApiView.as_view(), name="profile")
]