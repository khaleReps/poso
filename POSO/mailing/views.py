from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.mail import get_connection
from django.core.mail import EmailMessage
from imaplib import IMAP4_SSL
import email
import datetime
from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.mail import get_connection
from django.utils import timezone
from django.shortcuts import render
from django.core.mail import get_connection

def email_view(request):
    # Get a connection to the email backend
    connection = get_connection()

    # Retrieve messages from the email backend
    messages = connection.get_and_delete_messages()

    # Loop through the messages and process them
    for message in messages:
        # Do something with the message, such as saving it to the database
        subject = message.subject
        body = message.body
        from_email = message.from_email
        recipients = message.to

    # Render a template with the processed messages
    context = {
        'messages': messages
    }
    return render(request, 'mailing/email.html', context)




def send_email(request):
    if request.method == 'POST':
        recipient = request.POST.get('recipient')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        sender = 'your-email-address'

        send_mail(subject, message, sender, [recipient], fail_silently=False)
        return render(request, 'mailing/email_sent.html')

    return render(request, 'mailing/send_email.html')

def dashboard(request):
    return render(request, 'mailing/dashboard.html')