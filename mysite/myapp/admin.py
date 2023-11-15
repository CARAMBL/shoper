from django.contrib import admin
from .models import Product


# Register your models here.

admin.site.register(Product)
admin.site.site_header = "Admin"
admin.site.site_title = "Admin"
admin.site.index_title = "AdminPanel"


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'disc')
    actions = ('make_zero',)

    def make_zero (self, request, queryset):
        queryset.update(price=0)



admin.site.unregister(Product)
admin.site.register(Product, ProductAdmin)



