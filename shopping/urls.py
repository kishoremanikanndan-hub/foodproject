from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('order/<int:id>/', views.order_now, name='order_now'),
    path('place-order/<int:id>/', views.place_order, name='place_order'),
]