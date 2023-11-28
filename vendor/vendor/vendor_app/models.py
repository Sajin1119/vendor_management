from django.db import models

# Create your models here.

class Vendor(models.Model):
    FullName = models.CharField(max_length=255)
    contact_details = models.CharField(max_length=255)
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)

class PurchaseOrder(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=50)
    vendor_reference = models.CharField(max_length=50)
    order_date = models.DateField()
    items = models.TextField()
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=20)

    class Meta:
        ordering = ['-order_date']

class VendorPerformance(models.Model):
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE)
    on_time_delivery_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    quality_rating = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    response_time = models.TimeField(null=True, blank=True)
    fulfilment_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
