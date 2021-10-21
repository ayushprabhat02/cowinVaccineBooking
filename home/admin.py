from django.contrib import admin
from .models import ayushVaccineSlot, Member_info_Class, VaccineSlot, vaccineBookingClass


class admin_member(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'uid',
                    'total_member', 'age', 'first_booking', 'second_booking']


admin.site.register(ayushVaccineSlot)
admin.site.register(Member_info_Class, admin_member)
admin.site.register(VaccineSlot)
admin.site.register(vaccineBookingClass)
