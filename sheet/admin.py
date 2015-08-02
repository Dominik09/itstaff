from django.contrib import admin
from sheet.models import Sheet, Comments

class SheetInline(admin.StackedInline):
    model = Comments
    extra = 1
class SheetAdmin(admin.ModelAdmin):
    fields = ['title', 'text', 'image']
    inlines = [SheetInline]
    #list_filter = ['date']

admin.site.register(Sheet, SheetAdmin)