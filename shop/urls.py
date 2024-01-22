from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from store.views import index, product_detail, add_to_cart, cart, delete_cart,about
from accounts.views import signup, logout_user, login_user

from shop import settings

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', about, name='contact'),
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path('login/', login_user, name='login'),
    path('cart/', cart, name='cart'),
    path('cart/delete/', delete_cart, name='delete-cart'),
    path('logout/', logout_user, name='logout'),
    path('product/<str:slug>', product_detail, name='product'),
    path('product/<str:slug>/add-to-cart', add_to_cart, name='add_to_cart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
