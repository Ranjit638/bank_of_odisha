from django.contrib import admin
from app.models import Accountuser, Records, Feedback

admin.site.site_header = 'Bank of Bharat'
# Register your models here.

admin.site.register(Accountuser)
admin.site.register(Records)
admin.site.register(Feedback)

