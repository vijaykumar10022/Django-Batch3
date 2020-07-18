from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header = "DOT AP Integrated Management System"
class fileCust(admin.ModelAdmin):
    list_filter = ("date_added",)
    list_display = ("filename", "date_added")
    
admin.site.register(adminfile, fileCust)
admin.site.register(aplsafile, fileCust)
admin.site.register(compliancefile, fileCust)
admin.site.register(itfile, fileCust)
admin.site.register(ruralfile, fileCust)
admin.site.register(srfile, fileCust)
admin.site.register(securityfile, fileCust)
admin.site.register(technologyfile, fileCust)
