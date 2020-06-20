from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
from frontend.models import Reservation

# Register your models here.
class HomePageAdmin(ImportExportModelAdmin):
       list_display = ("id", "Upcoming_events", "Achieve_image", "achieve")
admin.site.register(HomePage, HomePageAdmin)
class BannerAdmin(ImportExportModelAdmin):
       list_display = ("id", "banner")
admin.site.register(Banner,BannerAdmin)
class TestimonialAdmin(ImportExportModelAdmin):
       list_display = ( "id", "image", "name", "city", "description")
admin.site.register(Testimonial,TestimonialAdmin)
class RecentPostAdmin(ImportExportModelAdmin):
       list_display = ( "id", "name", "image",'date')
admin.site.register(RecentPost,RecentPostAdmin)
class TeamAdmin(ImportExportModelAdmin):
       list_display = ( "id", "name", "image",'designation')
admin.site.register(Team,TeamAdmin)
class GalleryAdmin(ImportExportModelAdmin):
       list_display = ( "id", "name", "image")
admin.site.register(Gallery,GalleryAdmin)
class EventAdmin(ImportExportModelAdmin):
       list_display = ( "id", "name", "image","date","address","description")
admin.site.register(Event,EventAdmin)
class SliderAdmin(ImportExportModelAdmin):
       list_display = ( "id", "image","date")
admin.site.register(Slider,SliderAdmin)
class ContactUsDetailAdmin(ImportExportModelAdmin):
       list_display = ( "id", "address","phone_no","support_phone_no","email")
admin.site.register(ContactUsDetail,ContactUsDetailAdmin)
