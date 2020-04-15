from django.contrib import admin

from .models import Page

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    #añadimos este nuevo campo que mostrara el titulo y el campo de ordenación
    #en el panel de administración
    list_display = ('title', 'order')

admin.site.register(Page, PageAdmin)