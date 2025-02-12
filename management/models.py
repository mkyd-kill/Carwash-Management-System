from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils import timezone

class BaseModel(models.Model):
    id = ShortUUIDField(unique=True, length=4, max_length=4, alphabet="0123456789", primary_key=True)
    updated_at = timezone.now()
    created_at = models.DateTimeField(default=timezone.now)

class SiteAdmin(BaseModel):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256)

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
    national_id = models.PositiveIntegerField(default=0)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=8, choices=GENDER, default="Male")
    contact = models.CharField(max_length=12)
    commission = models.PositiveIntegerField(default=0)
    salary = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS, default="Active")
    role = models.CharField(max_length=50)
    department = models.CharField(max_length=50)

class Services(BaseModel):
    STATUS = (
        ('offered', 'Offered'),
        ('not offered', 'Not Offered')
    )
    AVAILABILITY = (
        ('available', 'Available'),
        ('unavailable', 'Unavailable')
    )
    name = models.CharField(max_length=50)
    cost = models.PositiveIntegerField(default=0)
    discount = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=15, choices=STATUS, default="Offered")
    availability = models.CharField(max_length=15, choices=AVAILABILITY, default="Available")

class Transactions(BaseModel):
    PAYMENTS = (
        ('mpesa', 'M-Pesa'),
        ('airtelmoney', 'Airtel Money'),
        ('cash', 'Cash')
    )
    carPlate = models.CharField(max_length=50)
    paymentMethod = models.CharField(max_length=20, choices=PAYMENTS)
    cost = models.PositiveIntegerField(default=0)
    discount = models.PositiveIntegerField(default=0)
    totalPaid = models.PositiveIntegerField(default=0)
    service = models.ForeignKey(Services, on_delete=models.CASCADE, null=False)
    employee = models.ForeignKey(Staff, on_delete=models.CASCADE, null=False)