from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save, sender=Student)
def notify_guardian_on_registration(sender, instance, created, **kwargs):
    if created:
        subject = "Student Registration Completed"
        message = (
            f"Dear {instance.guardian_name},\n\n"
            f"We are pleased to inform you that {instance.full_name} has successfully registered.\n\n"
            f"Regards,\nSchool Administration"
        )
        recipient = instance.guardian_email

        # Example using email; you could also send SMS using Twilio or other gateway
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [recipient],
            fail_silently=True,
        )
