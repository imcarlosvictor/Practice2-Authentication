from django.contrib import admin

from .models import Accounts


# Register your models here.
@admin.register(Accounts)
class AccountsAdmin(admin.ModelAdmin):
    fields = ('username', 'email')
    list_display = ('username', 'email', 'created')
    list_filter = ('created', )
    search_field = ('username', )
    date_hierarchy = 'created'
