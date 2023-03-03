from django.contrib import admin
from .models import Students

# Register your models here.
class adminStudent(admin.ModelAdmin):
    list_display = ["registration_number", "first_name", "last_name"]

admin.site.register(Students, adminStudent)