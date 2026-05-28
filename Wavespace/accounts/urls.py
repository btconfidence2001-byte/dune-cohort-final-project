from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('buyer/', views.buyer_start, name='buyer_start'),
    path('seller/', views.seller_start, name='seller_start'),
    path('staff-panel/', views.staff_panel, name='staff_panel'),
]
