from django.contrib import admin
from django.urls import path, include
from . import views
from products.views import ProductListView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductListView.as_view(), name='index'),
    path('user/login', views.login_view, name='login_view'),
    path('user/logout', views.logout_view,name='logout_view'),
    path('user/register', views.register_view,name='register_view'),
    path('products/', include('products.urls'))

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
