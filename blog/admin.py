from django.contrib import admin
from .models import User, Entry, Syain,Syain2


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Entry)
class Entry(admin.ModelAdmin):
    pass


@admin.register(Syain)
class Syain(admin.ModelAdmin):
    pass


@admin.register(Syain2)
class Syain2(admin.ModelAdmin):
    pass
