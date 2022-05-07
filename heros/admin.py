from django.contrib import admin
from .models import Hero, Specifications


class HeroAdmin(admin.ModelAdmin):
    list_display = ('id', 'hero_name', 'fraction', 'named_item_recommended',
                    'furniture_recommended', 'engraving_recommended',)
    list_display_links = ('id', 'hero_name')
    search_fields = ('hero_name',)


class SpecificationsAdmin(admin.ModelAdmin):
    list_display = ('hero', 'named_item', 'furniture', 'engraving',
                    'evolution',
                    'hair', 'date_update_specifications',)
    list_display_links = ('hero', )
    search_fields = ('hero',)
    list_editable = ('hair',)
    list_filter = ('hair',)


admin.site.register(Hero, HeroAdmin)
admin.site.register(Specifications, SpecificationsAdmin)

