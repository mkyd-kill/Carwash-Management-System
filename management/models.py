from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils import timezone

class BaseModel(models.Model):
    id = ShortUUIDField(unique=True, length=4, max_length=4, alphabet="0123456789", primary_key=True)
    updated_at = timezone.now()
    created_at = models.DateTimeField(default=timezone.now)

class SiteAdmin(BaseModel):
    username = models.CharField(max_length=100)
    hashed_password = models.CharField(max_length=256)

class StaffManagement(BaseModel):
    role = models.CharField(max_length=50)
    department = models.CharField(max_length=50)

class Staff(BaseModel):
    GENDER = (
        ('Male', 'm'),
        ('Female', 'f')
    )
    STATUS = (
        ('Active', 'active'),
        ('Inactive', 'inactive')
    )
    name = models.CharField(max_length=100)
    national_id = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=8, choices=GENDER, default="Male")
    contact = models.CharField(max_length=12)
    commission = models.PositiveIntegerField(default="0712345678")
    salary = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS, default="Active")
    role = models.CharField(max_length=50)
    department = models.CharField(max_length=50)

class Transactions(BaseModel):
    vehicle = models.CharField(max_length=50)

class Services(BaseModel):
    STATUS = (
        ('Offered', 'offered'),
        ('Not Offered', 'not')
    )
    AVAILABILITY = (
        ('Available', 'available'),
        ('Unavailable', 'unavailable')
    )
    name = models.CharField(max_length=50)
    cost = models.PositiveIntegerField(default=0)
    discount = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=15, choices=STATUS, default="Offered")
    availability = models.CharField(max_length=15, choices=AVAILABILITY, default="Available")