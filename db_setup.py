from django.contrib.auth.models import User

User.objects.all().delete()


User.objects.create_superuser(
    username = 'harihari',
    email = '',
    password = 'harihari'
)

User.objects.create_user(
    username = '123412341234',
    password = 'harihari'
)