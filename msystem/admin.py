from django.contrib import admin
from .models import Member_info, Program, Branch, Barangay_report, Member_report


admin.site.register(Member_info)
admin.site.register(Program)
admin.site.register(Branch)
admin.site.register(Barangay_report)
admin.site.register(Member_report)
