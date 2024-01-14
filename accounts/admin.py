from django.contrib import admin

from accounts.models import Shopper

# Afficher les utilisateurs dans Admin.
admin.site.register(Shopper)