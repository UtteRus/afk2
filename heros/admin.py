from django.contrib import admin
from .models import Hero, Specifications


class HeroAdmin(admin.ModelAdmin):
    list_display = ('pk', 'hero_name', 'fraction', 'named_item_recommended',
                    'furniture_recommended', 'engraving_recommended',)
    list_display_links = ('pk', 'hero_name')
    search_fields = ('hero_name', )


class SpecificationsAdmin(admin.ModelAdmin):
    list_display = ('user', 'hero', 'named_item', 'furniture', 'engraving',
                    'evolution', 'hair', 'date_update_specifications', )
    list_display_links = ('hero', )
    search_fields = ('hero', )
    list_editable = ('hair', )
    list_filter = ('hair', 'hero__fraction', 'user__username')


admin.site.register(Hero, HeroAdmin)
admin.site.register(Specifications, SpecificationsAdmin)

admin.site.site_title = 'AFK ARENA'
admin.site.site_header = 'AFK ARENA'

