from django.conf import settings
from django.core.mail import send_mail


def send_account_activation_email(email, email_token):
    # return
    subject = "Verify your account for further process.."
    email_from = settings.EMAIL_HOST_USER
    message = f"Click in the link below to verify http://127.0.0.1:8000/accounts/activate/{email_token}"

    send_mail(subject, message, email_from, [email])