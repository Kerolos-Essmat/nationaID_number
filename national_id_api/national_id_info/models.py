from django.db import models

# Create your models here.
class APIAccessLog(models.Model):
    request_path = models.CharField(max_length=500, null=True, blank=True)
    access_time = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=150, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    execution_time = models.FloatField(help_text="Request duration in seconds", null=True, blank=True)
    status_code = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return f"Accessed National ID: {self.national_id} at {self.access_time}"