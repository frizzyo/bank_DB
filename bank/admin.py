from django.contrib import admin
from .models import CreditType, Credit, Client

# Register your models here.
admin.site.register(CreditType)
admin.site.register(Credit)
admin.site.register(Client)
