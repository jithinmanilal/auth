from django.urls import path
from .views import HomeView, CustomLoginView, DasboardView, CustomRegistrationView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', DasboardView.as_view(), name='dashboard'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', CustomRegistrationView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
