# Dashboard/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Payment

@receiver(post_save, sender=Payment)
def send_payment_notification_to_headteacher(sender, instance, created, **kwargs):
    if created:  # only send when a new Payment is created
        subject = "New Student Payment Received"
        message = f"""
Dear Guardian/Parent,

A payment has been made in the system.

Student: {instance.student.full_name}
Amount: UGX {instance.amount}
Date: {instance.date.strftime('%Y-%m-%d %H:%M:%S')}

Best regards,
REGIS High School Finance Portal
"""
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [settings.HEADTEACHER_EMAIL],
            fail_silently=False
        )
