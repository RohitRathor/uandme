from django.shortcuts import render
from django.http import HttpResponse
from backend.models import *
from frontend.forms import BookingForm
# Create your views here.
def index(request):
    data = HomePage.objects.get()
    data.achieve = Convert(data.achieve)
    testimonial = Clients()
    banner = banners()
    recentPosts = recentPost()
    team_data = team()
    slider_data = sliders()
    contactUsDetail = contact_us_detail()
    return render(request, "index.html",{'data':data,'testimonial':testimonial,'banner':banner,'recentPosts':recentPosts,'team':team_data,'slider_data':sliders,'contactUsDetail':contactUsDetail})

def gallery(request):
    recentPosts = recentPost()
    images = Gallery.objects.all()
    contactUsDetail = contact_us_detail()
    return render(request,"gallery.html",{'images':images,'recentPosts':recentPosts,'contactUsDetail':contactUsDetail})
    
def events(request):
    recentPosts = recentPost()
    data = Event.objects.all()
    contactUsDetail = contact_us_detail()
    return render(request,"events.html",{'recentPosts':recentPosts,"data":data,'contactUsDetail':contactUsDetail})

def about(request):
    recentPosts = recentPost()
    contactUsDetail = contact_us_detail()
    return render(request, "about.html",{'recentPosts':recentPosts,'contactUsDetail':contactUsDetail})

def contact(request):
    recentPosts = recentPost()
    contactUsDetail = contact_us_detail()
    return render(request,"contact.html",{'recentPosts':recentPosts,'contactUsDetail':contactUsDetail})

def eventDetails(request):
    recentPosts = recentPost()
    contactUsDetail = contact_us_detail()
    return render(request,"event-details.html",{'recentPosts':recentPosts,'contactUsDetail':contactUsDetail})
def singleBlog(request):
    recentPosts = recentPost()
    contactUsDetail = contact_us_detail()
    return render(request,"single-blog.html",{'recentPosts':recentPosts,'contactUsDetail':contactUsDetail})
def booking(request):
    if request.method == 'POST':
        form = Reservation(request.POST)
        query = form.save()
        if request.FILES:
            query.file = request.FILES['file']
            file_type = query.file.url.split('.')[-1]
            file_type = file_type.lower()
            query.save()
        else:
            query.save()            
            return render(request,"contact.html",{'message':"Query Successfully Sent, We Will Contact You By Email"})
    else:
        return render(request, 'contact.html',{'message_fail':"Sorry! Something Went Wrong"})
def Convert(string):
    li = list(string.split("."))
    return li
def Clients():
    data = Testimonial.objects.values('image','name','city','description').all()
    return data
def banners():
    data = Banner.objects.values('banner').all()
    return data
def recentPost():
    data = RecentPost.objects.values('name','image','date')
    return data
def team():
    data = Team.objects.values('name','image','designation')
    return data
def sliders():
    data = Slider.objects.values('image','date')
    return data
def contact_us_detail():
    data = ContactUsDetail.objects.values('support_phone_no','phone_no','address','email').get()
    return data

def booking_form(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            query = form.save()
            query.save() 
            return render(request,"contact.html",{'message':"Query Successfully Sent, We Will Contact You By Email"})
        else:
            return render(request,"contact.html",{'message-fail':"Sorry! Something Went Wrong"})
    else:
        return render(request, 'contact.html',{'message_fail':"Sorry! Something Went Wrong"})

