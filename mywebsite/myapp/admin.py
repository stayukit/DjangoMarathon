from django.contrib import admin
from django.utils import timezone
from .models import Product, Categorie, Staff, CustomerForm, ProductStock

class AdminViewCreateUpdate(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('_title', 'Create_at', 'Update_at')
    
    def Create_at(self, obj):
        get_time = timezone.localtime(obj.created_at).strftime("%Y-%m-%d %H:%M:%S")
        return get_time
    
    def Update_at(self, obj):
        get_time = timezone.localtime(obj.updated_at).strftime("%Y-%m-%d %H:%M:%S")
        return get_time
    
    
admin.site.register(Categorie)
admin.site.register(Product, AdminViewCreateUpdate)
admin.site.register(Staff)
admin.site.register(CustomerForm, AdminViewCreateUpdate)
admin.site.register(ProductStock)