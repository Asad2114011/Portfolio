from django.shortcuts import render,redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def contact_view(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            contact= form.save()

            send_mail(
                subject=f"New Contact Message from {contact.name}",
                message=f"""
                    Name:{contact.name}
                    Email:{contact.email}
                    Message:
                            {contact.message}
                    """,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=False,
            )

            return redirect('home')
    else:
        form=ContactForm()
        
    return redirect('home')
