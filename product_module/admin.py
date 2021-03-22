from django.contrib import admin
from .models import CartItem
admin.site.register(CartItem)

# Register your models here.
from .models  import Brand, Category, Product

admin.site.register(Brand)
admin.site.register(Category)

class ProductAdmin(admin.ModelAdmin):
    list_display = ["image_tag","name","price","brand","category"]
    search_fields=["name","brand__name","category__name","price",]
    list_filter = ["brand", "category",]
    #readonly_fields = []

admin.site.register(Product , ProductAdmin)
    


 