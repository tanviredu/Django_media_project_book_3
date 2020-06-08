from django.urls import path
from . import views

app_name='article'

urlpatterns = [
        path('login',views.auth_login,name='auth_login'),
        path('accounts/auth/',views.auth_view,name='auth_view'),
        path('accounts/loggedin/',views.logged_in,name='logged_in'),
        path('accounts/invalid/',views.invalid_login,name='invalid_login'),
        path('accounts/loggedout/',views.logged_out,name='logged_out'),
        path('accounts/register/',views.register_user,name='register_user'),
]
