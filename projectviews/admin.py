from django.contrib import admin

from .models import Profile,Projects, Review

admin.site.register(Profile)
admin.site.register(Projects)
admin.site.register(Review)