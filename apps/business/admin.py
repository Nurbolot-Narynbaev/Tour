from django.contrib import admin

from django.contrib import admin

from .models import(
    Company,
    Guide
)

admin.site.register({Company, Guide })