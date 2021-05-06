# Created
from django.urls import path
from authenticate import views

urlpatterns = [
    # path("authn/", views.authn, name="authn"),
    path("signup/", views.signupuser, name="signupuser"),
    path("signin/", views.signinuser, name="signinuser"),
    path("logout/", views.logoutuser, name="logoutuser"),

    # path("test1/", views.test1, name="test1"),
    path("", views.index, name="index"),
]
