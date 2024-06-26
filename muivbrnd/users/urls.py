from django.urls import path

from users import views

app_name = "users"

urlpatterns = [
    path("login/", views.login, name="login"),
    path("registration/", views.registration, name="registration"),
    path("profile/", views.profile, name="profile"),
    path('profile/<slug:profile_slug>', views.profile_menu, name='profile_menu'),
    path('users-cart/', views.users_cart, name='users-cart'),
    path("logout/", views.logout, name="logout"),
]

# ngrok http http://localhost:8000