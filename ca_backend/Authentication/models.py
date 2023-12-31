from django.db import models
from django.contrib.auth.models import AbstractBaseUser, Group

# Create your models here.

ROLE_CHOICES = (
    (3, 'Admin'),
    (2, 'Staff'),
    (1, 'User'),
)

STATUS_CHOICES = (
    ('P', 'Pending'),
    ('V', 'Verified'),
    ('D', 'Deleted')
)
class UserAccount(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    role = models.IntegerField(choices=ROLE_CHOICES, default=1)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    college = models.CharField(max_length=200, blank=False, null=False)
    year = models.IntegerField(blank=False, null=False)
    phone_no = models.CharField(max_length=10, blank=False, null=False)
    whatsapp_no = models.CharField(max_length=10, blank=False, null=False)
    postal_address = models.TextField()
    pin_code = models.IntegerField()
    why_choose = models.TextField()
    were_you_ca = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]