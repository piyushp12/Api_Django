from django.contrib import admin
from . models import Students

# Register your models here.
admin.site.register(Students)
class StudentAdmin(admin.ModelAdmin):
    fields = [ 'name', 'cls', 'avatar']
