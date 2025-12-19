from django.http import HttpResponse
from django.shortcuts import render
from ourservice.models import Contactform
from ourservice.models import About_d
from ourservice.models import Product_d

def HomePage(request):
    about_details = About_d.objects.all()
    product_details = Product_d.objects.all()
    data={
        'about_details': about_details,
        'product_details': product_details,
    }
    
    return render(request,'index.html',data)

def about(request):
    about_details = About_d.objects.all()
    data={
        'about_details': about_details,
    }
    return render(request,'about.html',data)

def service(request):
    return render(request,'service.html')

def product(request):
    return render(request,'product.html')

def error(request):
    return render(request,'404.html')

def contact(request):
    msg = ""
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        # Process the form data (e.g., save to database, send email, etc.)
        Contactform.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        msg = "Your message has been sent successfully!"
    return render(request,'contact.html', {"msg": msg})

def team(request):
    return render(request,'team.html')

def testimonial(request):
    return render(request,'testimonial.html')