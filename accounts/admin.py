from django.contrib import admin

from .models import *


class PatientAdmin(admin.ModelAdmin):
    list_display = ('p_id','user','phone','email','address','birth_date','guardian',)
    list_display_links = ('p_id', 'user')
    search_fields = ('user', 'phone', 'email')
    list_per_page = 20

admin.site.register(Patient,PatientAdmin)

class InstructorAdmin(admin.ModelAdmin):
    list_display = ('in_id','user','phone','email','address','qualification')
    list_display_links = ('in_id', 'user')
    search_fields = ('user', 'phone', 'email')
    list_per_page = 20

admin.site.register(Instructor,InstructorAdmin)

class MyWorksAdmin(admin.ModelAdmin):
    list_display = ('user','title','video')
    list_display_links = ('user', 'title','video')
    search_fields = ('user', 'title', 'author')
    list_per_page = 20

admin.site.register(MyWorks,MyWorksAdmin)
admin.site.register(Event)
