from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):

    list_display = [field.name for field in Profile._meta.fields]
    search_fields = [field.name for field in Profile._meta.fields]
    list_filter = ['name', 'email']

    # list_display = ["name", "email"]
    # exclude = ["email"]
    # list_filter = ['']
    # search_fields = ['category', 'subCategory', 'suggestKeyword']
    # inlines = [FieldMappingInline]
    # fields = [] # exclude fields in one item

    class Meta:
        model = Profile


admin.site.register(Profile, ProfileAdmin)

