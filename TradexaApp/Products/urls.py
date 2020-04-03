from django.urls import path
from.import views
urlpatterns = [
    path('Product/', views.Product,name='Product'),
    path("Product/user/Logout", views.Logout,name='Product/user/Logout'),
    
]