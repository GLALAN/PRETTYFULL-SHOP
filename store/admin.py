from django.contrib import admin
from store.models import Product, Order, Cart

# Je conserve le model de django.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Cart)