from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.decorators.cache import never_cache

from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, email_verification, UserPasswordResetView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', never_cache(LoginView.as_view(template_name='users/login.html')), name='login'),
    path('logout/', never_cache(LogoutView.as_view()), name='logout'),
    path('register/', never_cache(RegisterView.as_view()), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('email-confirm/<str:token>/', never_cache(email_verification), name='email-confirm'),
    path('password-reset/', never_cache(UserPasswordResetView.as_view()), name='password-reset'),
]
