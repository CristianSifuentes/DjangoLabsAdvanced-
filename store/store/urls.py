from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('user/login', views.login_view, name='login_view'),
    path('user/logout', views.logout_view,name='logout_view'),
    path('user/register', views.register_view,name='register_view')

]
