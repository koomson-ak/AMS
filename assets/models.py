from django.db import models
from django.db.models import Q
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class Asset(models.Model):
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('in_use', 'In Use'),
        ('maintenance', 'Under Maintenance'),
        ('lost', 'Lost'),
        ('retired', 'Retired'),
    )
    
    serial_no = models.CharField(
        max_length=10,
        unique = True,
        db_index = True,
        help_text='The serial number of the asset'
    )
    asset_category = models.CharField(max_length=100)
    asset_type = models.CharField(max_length=100)
    owner = models.Charfield(max_length = 100,
                             default = 'Unassigned',
                             blank = False,
                             help_text = 'The staff who owns this asset')
    department = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @classmethod
    def search_fields(cls, query):
        if query:
            return cls.objects.filter(
                Q(serial_no__icontains=query) |
                Q(asset_category__icontains=query) |
                Q(asset_type__icontains=query) |
                Q(owner__icontains=query) |
                Q(department__icontains=query) |
                Q(status__icontains=query)
            )
        else:
            return cls.objects.all()
    
    @property
    def last_updated(self):
        return self.updated_at.strftime('%Y-%m-%d %H:%M')
    
    @property
    def created_date(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M')
    
    def __str__(self):
        return self.serial_no
    