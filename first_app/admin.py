from django.contrib import admin

# Register your models here.

from first_app.models import Student, College, Album, Track

admin.site.register([Student, College, Album, Track])