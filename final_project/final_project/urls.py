from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from shopping import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url('home/', views.home, name='home'),
    url('cart/', views.cart, name='cart'),
    url('products/', views.products, name='products'),
    path('admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
