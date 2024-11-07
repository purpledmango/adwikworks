from django.urls import path
from .views import home_view, register_user
urlpatterns=[
    path("", home_view),
    path("register/", register_user, name="register_user")
    # path("/signup")
]