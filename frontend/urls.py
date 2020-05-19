from django.urls import path,include
from . import views
from uandmecreation import settings
from django.contrib.staticfiles.urls import static
urlpatterns = [
    path('',views.index,name="index"),
    path('index',views.index,name="index"),
    path('gallery',views.gallery,name="gallery"),
    path('events',views.events,name="events"),
    path('about-us',views.about,name="about-us"),
    path('contact',views.contact,name="contact"),
    path('event-details',views.eventDetails,name="event-details"),
    path('single-blog',views.singleBlog,name="single-blog"),
    path('booking',views.booking_form,name="booking"),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
