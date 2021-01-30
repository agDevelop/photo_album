from django.contrib import admin
from .models import Album, Size, Binding, Template
from import_export.admin import ImportExportModelAdmin


def make_hard_binding(modeladmin, request, queryset):
    queryset.update(binding='1')
make_hard_binding.short_description = "Изменить на твердый переплёт"

def make_soft1_binding(modeladmin, request, queryset):
    queryset.update(binding='2')
make_soft1_binding.short_description = "Изменить на мягкий переплёт на скрепке"

def make_soft2_binding(modeladmin, request, queryset):
    queryset.update(binding='3')
make_soft2_binding.short_description = "Изменить на мягкий переплёт на пружине"


@admin.register(Album)
class AlbumAdmin(ImportExportModelAdmin):
    list_display = ('title', 'size', 'binding', 'pages', 'template')
    list_display_links = ('title',)
    list_filter = ("size", "template", )
    search_fields = ("title__startswith",)
    actions = [make_hard_binding, make_soft1_binding, make_soft2_binding]
    pass


admin.site.register(Size)
admin.site.register(Binding)
admin.site.register(Template)