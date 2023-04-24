from django.urls import path
from base.views import order_views as views
from base.views.order_views import download_file

urlpatterns = [

    path('', views.getOrders, name='orders'),
    path('add/', views.addOrderItems, name='orders-add'),
    path('myorders/', views.getMyOrders, name='myorders'),

    path('<str:pk>/deliver/', views.updateOrderToDelivered, name='order-delivered'),

    path('<str:pk>/', views.getOrderById, name='user-order'),
    path('<str:pk>/pay/', views.updateOrderToPaid, name='pay'),
    path('<str:pk>/download/<str:file_path>/', download_file.as_view(), name='download_file'),
    path('<str:pk>/delete/', views.deleteOrder, name='delete-order'),

]
