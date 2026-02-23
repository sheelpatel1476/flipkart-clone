from django.db import models

class Mobile(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='mobiles/', blank=True, null=True)
    ram = models.CharField(max_length=50)
    storage = models.CharField(max_length=50)
    display = models.CharField(max_length=100)
    battery = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.name}"

    class Meta:
        ordering = ['-created_at']
