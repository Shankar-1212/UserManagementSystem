from django.contrib import admin
from django.urls import path
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login_user'),
    path('profile/', views.retrieve_user_profile, name='retrieve_user_profile'),
    path('update/', views.update_user_profile, name='update_user_profile'),
    path('delete/', views.delete_user_profile, name='delete_user_profile'),
]

