from django.urls import path

from .views import RegisterCreateView, Login, Profile, Logout


urlpatterns = [
    path('register/', RegisterCreateView.as_view(), name="register"),
    path('login/', Login.as_view(), name="login"),
    path('profile/', Profile.as_view(), name="profile"),
    path('logout/', Logout.as_view(), name="logout"),


]