from django.http import HttpResponse
from django.shortcuts import render
from ourservice.models import Contactform
from ourservice.models import About_d
from ourservice.models import Product_d
from ourservice.models import Team_d
from ourservice.models import Review_d
from ourservice.models import blog_d
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
import requests

def HomePage(request):
    about_details = About_d.objects.all()
    product_details = Product_d.objects.all()
    team_details = Team_d.objects.all()
    review_details = Review_d.objects.all()
    data={
        'about_details': about_details,
        'product_details': product_details,
        'team_details': team_details,
        'review_details': review_details,
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


from django.shortcuts import render
from ourservice.models import Contactform
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def contact(request):
    msg = ""
    msg_class = ""

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Save in DB
        Contactform.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        try:

            # ====================
            # 1️⃣ Send email to ADMIN
            # ====================
            admin_html = render_to_string("admin_mail.html", {
                "name": name,
                "email": email,
                "subject": subject,
                "message": message
            })

            email_admin = EmailMultiAlternatives(
                subject=f"New Contact Form Submission: {subject}",
                body="New form received",
                from_email="yourgmail@gmail.com",
                to=["yourgmail@gmail.com"]
            )
            email_admin.attach_alternative(admin_html, "text/html")
            email_admin.send(fail_silently=False)

            # ====================
            # 2️⃣ Send email to USER
            # ====================
            user_html = render_to_string("user_thankyou.html", {
                "name": name,
            })

            email_user = EmailMultiAlternatives(
                subject="Thank you for contacting us!",
                body="We received your message.",
                from_email="yourgmail@gmail.com",
                to=[email]
            )
            email_user.attach_alternative(user_html, "text/html")
            email_user.send(fail_silently=False)

            msg = "Form Submitted Successfully!"
            msg_class = "success"

        except Exception as e:
            print("Email Error:", e)
            msg = "Form saved but email sending failed!"
            msg_class = "error"

    return render(request, "contact.html", {
        "msg": msg,
        "msg_class": msg_class
    })


def team(request):
    return render(request,'team.html')

def testimonial(request):
    return render(request,'testimonial.html')

def blog(request):
    blog_details=blog_d.objects.all()
    blog_detail = {
        'blog_details': blog_details
    }
    return render(request,'blog.html',blog_detail)



def CakeApi(request):
    api_url = "https://forkify-api.herokuapp.com/api/v2/recipes?search=cake"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        recipes = data.get('data', {}).get('recipes', [])

    else:
        recipes = []

    return render(request, 'print_json.html', {'recipes': recipes})







