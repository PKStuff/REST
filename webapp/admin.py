from django.contrib import admin
from .models import employee

@admin.register(employee)
class AdminEmployee(admin.ModelAdmin):

    list_display = ['name','lname','email','phone']
    #list_editable = ('name','lname','phone')

