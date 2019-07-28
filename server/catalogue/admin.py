from django.contrib import admin
from .models import Category, Brand, BrandAssociations


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'url', 'logo_url', 'single_liner', 'cta_text', 'date_created', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_created', )


class BrandAssociationAdmin(admin.ModelAdmin):
    list_display = ('source', 'destination', 'date_created', )
    ordering = ['source', 'destination']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(BrandAssociations, BrandAssociationAdmin)
