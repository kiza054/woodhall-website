from time import sleep

from celery import shared_task
from django.db.models import Q

from accounts.models import User


@shared_task
def sleepy(duration):
    sleep(duration)
    return None

@shared_task
def send_email_task():
    sleep(10)
    sender = os.environ.get('EMAIL_USER')
    subject = '1st Woodhall Cubs Blog | New Blog Post'
    text_content = 'Hello there, there has been a new post published on the blog. Check it out!'
    html_content = '<p>Hello there, there has been a new post published on the blog. Check it out!</p>'
    recipients = []
    
    #for users in User.objects.filter(Q(section='Cubs') | Q(second_section='Cubs')):
    for users in User.objects.filter(is_superuser=True):
        recipients.append(users.email)

    msg = EmailMultiAlternatives(subject, text_content, sender, recipients)
    msg.attach_alternative(html_content, "text/html")
    msg.send(fail_silently=False)

    return None