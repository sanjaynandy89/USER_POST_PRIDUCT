from django.urls import path
from.import views
urlpatterns = [
    path('', views.user,name='user'),
    path('Register', views.Registration,name='Registration'),
    path("Login", views.Login,name='Login'),
    path("Logout", views.Logout,name='Logout'),
    path("Post", views.CreatePost,name='Post'),
]
