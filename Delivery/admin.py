from django.contrib import admin

# Register your models here.
from .models import Goods

@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
#admin.site.register(Goods)

