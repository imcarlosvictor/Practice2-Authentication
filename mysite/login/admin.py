from django.contrib import admin

from .models import MyUser


# Register your models here.
@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    fields = ('username', 'first_name', 'last_name', 'email')
    list_display = ('username', 'first_name', 'last_name', 'email', 'created')
    list_filter = ('created', )
    search_field = ('username', )
    date_hierarchy = 'created'
