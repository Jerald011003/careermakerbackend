from django.urls import path
from base.views import heart_views as views

urlpatterns = [
    path('createheartlist/', views.addHeartUser, name='add_heart_user'),
    path('heartlist/', views.getHeartList, name='heartlist'),
    path('', views.getAllHeartList, name='allheartlist'),
    path('update/<str:pk>/', views.update_hearts, name="update-hearts"),
    path('delete/<str:pk>/', views.delete_hearts, name="delete-heart"),
    path('upload/', views.uploadResume, name="image-resume"),

]
