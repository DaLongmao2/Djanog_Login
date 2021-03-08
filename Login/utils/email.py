import time
from Pro import settings
from django.core.mail import send_mail


def send_email(subject, html_message, message, recipient, from_email=settings.EMAIL_HOST_USER, fail_silently=False):
    try:
        send_mail(
            subject=subject,
            html_message=html_message,
            message=message,
            from_email=from_email,
            recipient_list=recipient,
            fail_silently=fail_silently
        )
        print('jjjjjjj')
        return True
    except:
        return False