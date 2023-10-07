from django.contrib import admin
from .models import banner,Registration,overview,gallery,amenities,walkthrough,know_your_locality,brochure,locality_map,Logo,configuration,Introduction
from .models import enquire_now
# from accounts.models import UserProfile
# Register your models here.

# admin.site.register(enquire_now)
admin.site.register(overview)
admin.site.register(configuration)
# admin.site.register(configuration1)
admin.site.register(gallery)
# admin.site.register(amenities)
admin.site.register(walkthrough)
admin.site.register(know_your_locality)
admin.site.register(locality_map)
admin.site.register(Logo)
admin.site.register(banner)
admin.site.register(Introduction)
admin.site.register(brochure)
admin.site.register(Registration)

@admin.register(enquire_now)
class EnquiryAdmin(admin.ModelAdmin):
    list_display=('name','Mobile_number','email','enquiry_type')
    ordering=('name',)
    search_fields=('name',)