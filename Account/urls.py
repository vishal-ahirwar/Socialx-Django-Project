from django.urls import path
from .views import SignUp, UserLogin,UserLogout
app_name='Account'
urlpatterns=[
    path('login/',UserLogin,name='login'),
    path('signup/',SignUp,name='signup'),
    path('logout/',UserLogout,name='logout'),
]
