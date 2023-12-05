from django.urls import path
from . import uiviews, authviews, apiviews

urlpatterns = [
    path('', uiviews.index, name="index"),
    path('login', authviews.loginUser, name="login"),
    path('logout', authviews.logoutUser, name="logout"),
    path('signup', authviews.signupUser, name="signup"),
    path('history', uiviews.viewHistory, name="history"),
    path('api/post_data/<str:username>', apiviews.PostData.as_view(), name="post-data")
]