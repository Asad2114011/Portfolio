from django.shortcuts import render,redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
import resend
import os
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.

def contact_view(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            contact= form.save()
            print('fetch working!')
            try:
                resend.api_key = os.getenv('RESEND_API_KEY')
                EMAIL_HOST_USER=os.getenv('EMAIL_HOST_USER')
                resend.Emails.send({
                    "from": "onboarding@resend.dev",
                    "to": EMAIL_HOST_USER,
                    "subject": f"New contact message from {contact.name}",
                    "text": f"Name: {contact.name}\nEmail: {contact.email}\nMessage: {contact.message}"
                })
                return JsonResponse({'success':True,'message':'Message sent successfully!'})
            except Exception as e:
                print(f"Email failed: {e}")
                return JsonResponse({'success': False, 'message': f'Something went wrong: {str(e)}'})

    else:
        return JsonResponse({'success':False,'message':'Invalid form submisson.'})
        
    return JsonResponse({'success':False,'message':'Invalid request.'})
