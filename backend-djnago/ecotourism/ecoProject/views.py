from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.

# def home(request):
#     return HttpResponse("EcoProject app is working inside ecotoursim project.")
def index(request):
    return render(request, 'ecoProject/index.html')

def about(request):
    return render(request, 'ecoProject/about.html')

def activities(request):
    return render(request, 'ecoProject/activities.html')

def contact(request):
    # The 'success' flag is no longer needed when using the messages framework
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Save to database
        Contact.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            message=message
        )
        # Add a success message to the request
        messages.success(request, "✅ Your message has been sent. Please check your email for confirmation!")
        
        # Send confirmation email to user
        subject = "Thank you for contacting Eco-Tourism Okayama!"
        body = f"Hi {first_name},\n\nThank you for your message:\n\"{message}\"\n\nWe will get back to you shortly.\n\nBest regards,\nEco-Tourism Okayama"
        sender = settings.EMAIL_HOST_USER
        recipient = [email]  # send to user

        send_mail(subject, body, sender, recipient, fail_silently=False)

        # The key fix: Redirect after a successful POST.
        # This prevents the form from re-submitting on page refresh.
        return redirect('contact')

    # For a GET request, just render the page
    return render(request, 'ecoProject/contact.html')

# The commented-out functions below are not needed
# def contact_success(request):
#     return render(request, "contact.html", {"success": True})
