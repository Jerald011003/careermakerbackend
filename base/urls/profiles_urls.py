from django.urls import path
from base.views import profiles_views as views

urlpatterns = [
    path('', views.get_profiles, name="profiles"),
    path('myprofiles/', views.get_user_profiles, name="my-profiles"),

    path('top/', views.get_top_profiles, name="top-profiles"),
    path('<str:pk>/', views.get_profile_details, name="profile"),
    path('profileitem/create/', views.create_profile, name="create-profile"),
    path('update/<str:pk>/', views.update_profile, name="update-profile"),
    path('delete/<str:pk>/', views.delete_profile, name="delete-profile"),
    path('<str:pk>/reviews/create/', views.create_profile_review, name="create-profile-review"),
    path('update/<str:pk>/', views.update_profile_review, name="update-profile-review"),
    path('delete/<str:pk>/', views.delete_profile_review, name="delete-profile-review"),
    path('profileitem/upload/', views.upload_image, name="upload-image"),
    path('profileitem/user/', views.get_user_profiles, name="user-profiles"),
]