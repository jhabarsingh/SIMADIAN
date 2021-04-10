from django.urls import path
from .views import ( 
    ItemListApiView,
    ItemCreateApiView,
    ItemUpdateDeleteApiView,
    CategoryUpdateApiView
)

app_name = 'commerce'

urlpatterns = [
    path('', ItemListApiView.as_view(), name='list'),
    path('create/', ItemCreateApiView.as_view(), name='create'),
    path('item/', ItemUpdateDeleteApiView.as_view(), name='item'),
    path('category/', CategoryUpdateApiView.as_view(), name='category'),
]