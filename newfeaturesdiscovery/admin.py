from django.contrib import admin

from newfeaturesdiscovery.models import MyDeafultFieldModel, Square

@admin.register(MyDeafultFieldModel)
class MyDeafultFieldModelAdmin(admin.ModelAdmin):
    list_display = ("age", "created", "circumference")
    list_editable = ("created", )
    list_display_links = ("age", )

@admin.register(Square)
class SquareAdmin(admin.ModelAdmin):
    list_display = ("side", "area")

# admin.site.register(MyDeafultFieldModel)
# admin.site.register(Square)