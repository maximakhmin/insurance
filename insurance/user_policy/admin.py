from django.contrib import admin
from .models import UserPolicy, Payment
# Register your models here.

admin.site.register(Payment)
admin.site.register(UserPolicy)