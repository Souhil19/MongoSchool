from .models import Student
from django.contrib import admin

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','birth_date','field')


admin.site.register(Student,StudentAdmin)



#https://stackoverflow.com/questions/69397039/pymongo-ssl-certificate-verify-failed-certificate-has-expired-on-mongo-atlas