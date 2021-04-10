from django.urls import path
from .views import ( 
    UsersListApiView,
    UserCreateApiView,
    UserRetrieveUpdateDeleteApiView
)

app_name = 'users'

urlpatterns = [
    path('', UsersListApiView.as_view(), name='list'),
    path('create/', UserCreateApiView.as_view(), name='create'),
    path('retrieve-update-delete/<slug:username>/', UserRetrieveUpdateDeleteApiView.as_view(), name='retrieve_update_delete')
]