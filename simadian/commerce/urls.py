from django.urls import path
from .views import ( 
    ItemListApiView,
    ItemCreateApiView,
    ItemUpdateDeleteApiView,
    CategoryDeleteApiView,
    CategoryCreateApiView,
    CategoryListApiView,
    MessageCreateApiView,
    MessageDeleteApiView,
    MessagesReceivedApiView,
    MessagesSentApiView
)

app_name = 'commerce'

urlpatterns = [
    path('', ItemListApiView.as_view(), name='list'),
    path('create/', ItemCreateApiView.as_view(), name='create'),
    path('item/', ItemUpdateDeleteApiView.as_view(), name='item'),
    path('category/', CategoryListApiView.as_view(), name='category'),
    path('category/create/', CategoryCreateApiView.as_view(), name='category-c'),
    path('category/delete/', CategoryDeleteApiView.as_view(), name='category-delete'),
    path('message/create/', MessageCreateApiView.as_view(), name='message_create'),
    path('message/delete/', MessageDeleteApiView.as_view(), name='message_update'),
    path('message/received/', MessagesReceivedApiView.as_view(), name='message_received'),
    path('message/sent/', MessagesSentApiView.as_view(), name='message_sent')

       
]