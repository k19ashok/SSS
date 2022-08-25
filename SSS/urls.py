from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
LOGOUT_REDIRECT_URL='home'
urlpatterns = [
    path('',views.home,name="home"),
    path('academics/',views.academics,name="academics"),
    path('infra/',views.infra,name="infra"),
    path('about/',views.about,name="about"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('counselling/',views.counselling,name="counselling"),
    path('application/',views.application,name="application"),
    path('submitted/',views.submitted,name="submitted"),
    path('userlogout/',LogoutView.as_view(next_page=LOGOUT_REDIRECT_URL),name="userlogout"),
]


