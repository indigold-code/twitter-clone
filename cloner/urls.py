from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('profile_list', views.profile_list, name='profile_list'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('update_user/', views.update_user, name='update_user'),
    path('chirp_fave/<int:pk>', views.favorite_chirp, name='chirp_fave'),
    path('show_chirp/<int:pk>', views.show_chirp, name='show_chirp'),
]
