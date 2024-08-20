from celery import shared_task
from user.models import GeneratePassword

@shared_task
def delete_generate_password():
    # GeneratePassword tozalab turish uchun
    
    GeneratePassword.objects.all().delete()
    