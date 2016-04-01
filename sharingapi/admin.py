from django.contrib import admin
from sharingapi.models import SharedItem, Item, Location, User

# Register your models here.

class SharedItemAdmin(admin.ModelAdmin):

    list_display = ['id', 'trade_type', 'trade_status', 'timestamp']

class ItemAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'category', 'description']


class LocationAdmin(admin.ModelAdmin):

    list_display = ['id', 'address', 'lat', 'lng']

class UserAdmin(admin.ModelAdmin):

    list_display = ['id', 'username', 'firstname', 'surname', 'email', 'phone', 'password']


admin.site.register(SharedItem, SharedItemAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(User, UserAdmin)
