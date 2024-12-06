from django.contrib import admin
from django.utils.html import format_html

from .models import Category, Product, Contact, Bucket, BucketProduct, Rating

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')  # Display the 'name' field in the admin list view



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # fields = ['title', 'description', 'price', 'discount_percent', 'is_active', 'count', 'image', 'category']
    # exclude = ["image", ]
    list_display = ['title', 'description', 'price', 'discount_percent', 'is_active', 'count', 'image_tag', 'category', 'created_by']
    list_display_links = ["title", "description", "price"]
    search_fields = ['title', 'category__name']
    list_filter = ['is_active', 'category']
    sortable_field_name = ['id', 'title']

    def image_tag(self, obj):
        return format_html(f"<img src='{obj.image.url}' width='150px' height='100px' />" if obj.image else "Surat mavjud emas")


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

admin.site.register(Bucket)
admin.site.register(Rating)

@admin.register(BucketProduct)
class BucketProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'bucket']
    list_filter = ['bucket']
