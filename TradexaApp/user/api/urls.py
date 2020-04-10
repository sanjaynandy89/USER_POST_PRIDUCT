from django.urls import path
from user.api import views
app_name='user'
urlpatterns = [
    path('Post/',views.PostList.as_view(),name='details'),
    
]