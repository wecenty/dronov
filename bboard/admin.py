from django.contrib import admin
from .models import Bb, Rubric


# Register your models here.

class BbAdmim(admin.ModelAdmin):
    list_display = ('title', 'content', 'published', 'price', 'rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content',)


admin.site.register(Bb, BbAdmim)
admin.site.register(Rubric)
