from django.contrib import admin

from catalog.models import Category, Product, Contacts, Feedback, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'discription',)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'address', 'phone_number', 'email_address',)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'phone_number', 'message',)
    list_filter = ('name',)
    search_fields = ('name', 'phone_number',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'number', 'name', 'is_current', 'product',)
    list_filter = ('product',)
    search_fields = ('name', 'number',)
