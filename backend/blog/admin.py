from django.contrib import admin
from .models import blog,contact
# Register your models here.
@admin.register(blog)
@admin.register(contact)
class StudentAdmin(admin.ModelAdmin):
       pass
