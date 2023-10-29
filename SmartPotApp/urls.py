from django.urls import path
from . import uiviews, authviews

urlpatterns = [
    path('', uiviews.index, name="index"),
    path('login', authviews.loginUser, name="login"),
    path('logout', authviews.logoutUser, name="logout"),
    path('signup', authviews.signupUser, name="signup"),
]