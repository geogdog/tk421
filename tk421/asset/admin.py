from django.contrib import admin

from asset.models import Asset

class AssetAdmin(admin.ModelAdmin):
    pass
admin.site.register(Asset, AssetAdmin)
