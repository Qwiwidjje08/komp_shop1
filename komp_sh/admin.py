from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

admin.site.register(Category)
admin.site.register(Brands)
admin.site.register(Comments)

@admin.register(Product)
class ProductClass(admin.ModelAdmin):
    list_display = ['name','price','brand','category','show_image']
    list_display_links=['name','brand']
    list_filter=['brand','category']
    list_editable=['price']

    def show_image(self,photo):
        if photo.img1:
            return mark_safe(f"<img src='{photo.img1.url}' width=100>")
        return None
    show_image.__name__='Suwret'


