import os
from django.http import FileResponse,HttpResponseNotFound
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
# from django.db.models import File
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from .forms import SubmitForm
# from .forms import LocationForm
from .models import banner,know_your_locality,walkthrough,amenities,brochure,enquire_now,overview,locality_map,gallery, Logo,configuration,Introduction,Registration


def registration(request):
    if request.method=="POST":
        post=enquire_now()
        post.name=request.POST['name']
        # post.Last_name=request.POST['last_name']
        post.Mobile_number=request.POST['mobile_number']
        post.email=request.POST['email']
        post.enquiry_type = request.POST['form_type']
        
        send_mail(
            'New form submission',
            f'Name:{post.name}\nMobile:{post.Mobile_number}\nEmail:{post.email}\nType:{post.enquiry_type}',
            settings.EMAIL_HOST_USER,
            [settings.RECIPIENT_ADDRESS],
            fail_silently=False,
        )
        post.save()
        return redirect("thank")
    else:
        return redirect("index")

def downloadenquiry(request):
    if request.method=="POST":
        post=enquire_now()
        post.name=request.POST['name']
        # post.Last_name=request.POST['last_name']
        post.Mobile_number=request.POST['mobile_number']
        post.email=request.POST['email']
        post.enquiry_type = request.POST['form_type']
        send_mail(
            'New form submission',
            f'Name:{post.name}\nMobile:{post.Mobile_number}\nEmail:{post.email}\nType:{post.enquiry_type}',
            settings.EMAIL_HOST_USER,
            [settings.RECIPIENT_ADDRESS],
            fail_silently=False,
        )
        post.save()
        return redirect("/download/")
    else:
        return redirect("index")
    
def thank(request):
    return render(request, "thankyou.html")
  
# def contact(request):
#     if request.method == 'GET':
#         form = SubmitForm()
          
#     else:
#         form = SubmitForm(request.POST)
#         if form.is_valid():
#             first_name=form.cleaned_data['first_name']
#             Last_name=form.cleaned_data['last_name']
#             Mobile_number=form.cleaned_data['mobile_number']
#             email=form.cleaned_data['email']
#             enquiry_type = form.cleaned_data['form_type']
        
#                 # send_email(first_name,Last_name,Mobile_number,email,enquiry_type,["mashigula@gmail.com"])
        
            
#     return render(request, 'index.html', {'form':form})


def index(request):
    pc_overview=overview.objects.first()
    lc_map=locality_map.objects.first()
    logos = Logo.objects.first()
    gallery_objects = gallery.objects.all()
    # img=gallery.objects.all()
    locality = know_your_locality.objects.all()
    video = walkthrough.objects.first()
    source=amenities.objects.all()
    config=configuration.objects.all()
    # configure=configuration1.objects.first()
    Banner=banner.objects.first()
    intro=Introduction.objects.first()
    brochures=brochure.objects.first()
    register=Registration.objects.all()
    return render(request, "index.html", {"Introduction":intro,"brochure":brochures,
        "banner":Banner,"configs":config,"sources":source,"galleries": gallery_objects, "localities": locality,
                                          "video": video,"overview":pc_overview,"lc_map":lc_map,
                                          "logos": logos,"registers":register})



def download_file(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'Budhera Bliss Brochure 03.pdf'
    filepath = BASE_DIR + '/Budheraapp/Files/' + filename
    try:
        print(filepath)
        pdf_file =  open(filepath, 'rb')
        response = FileResponse(pdf_file)
        response['Content-Disposition'] = 'attachment; filename="broucher.pdf"'

        return response   
    except FileNotFoundError:
        return HttpResponseNotFound("PDF file not found.")

# def download_pdf_file(request, filename=''):
#         # Define Django project base directory
#         BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#         # Define the full file path
#         filepath = BASE_DIR + '/Brigadeapp/Files/' + filename
#         # Open the file for reading content
#         path = open(filepath, 'rb')
#         # Set the mime type
#         mime_type, _ = mimetypes.guess_type(filepath)
#         # Set the return value of the HttpResponse
#         response = HttpResponse(path, content_type=mime_type)
#         # Set the HTTP header for sending to browser
#         response['Content-Disposition'] = "attachment; filename=%s" % filename
#         # Return the response value
#         return response

def privacy(request):
    logos = Logo.objects.first()
    return render(request,"policy.html",{"logos":logos})


# def download_file(request, file_id):
#     file = get_object_or_404(File, pk=file_id)
#     with open(file.file_path, 'rb') as f:
#         response = HttpResponse(f.read(), content_type=file.content_type)
#         response['Content-Disposition'] = 'attachment; filename="%s"' % file.file_name
#         return response

# file = File.objects.get(name='myfile.pdf')
# file_id = file.id


# file_id = '1234567890abcdef'
# download_url = reverse('download_file', args=[file_id])

# from django.http import HttpResponse, Http404
# from django.conf import settings
# import os

# def download_file(request, file_path):
#     file_full_path = os.path.join(settings.MEDIA_ROOT, file_path)
    
#     if os.path.exists(file_full_path):
#         with open(file_full_path, 'rb') as file:
#             response = HttpResponse(file.read(), content_type='application/octet-stream')
#             response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_full_path)
#             return response
#     else:
#         raise Http404
