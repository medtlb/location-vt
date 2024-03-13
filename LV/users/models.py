from django.db import models
from django.contrib.auth.models import User

class CategoryCar(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    picture = models.ImageField(upload_to='car_pictures/', blank=True, null=True)
    category_car = models.ForeignKey(CategoryCar, on_delete=models.CASCADE, related_name='cars')

    def __str__(self):
        return f"{self.brand} {self.model}"
    
class AvailabilityCar(models.Model):
    car = models.OneToOneField(Car, on_delete=models.CASCADE)
    quantity_available = models.IntegerField()

    def __str__(self):
        return f"{self.car} - {self.quantity_available}"

class Reservation(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    STATUS_CHOICES = [
        ('Accepted', 'Accepted'),
        ('Not Accepted', 'Not Accepted'),
        ('Waiting', 'Waiting'),
    ]
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='Waiting')

    def __str__(self):
        return f"Reservation for {self.car} by {self.user}"

# class Reservation(models.Model):
#     car = models.ForeignKey(Car, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)
#     STATUS_CHOICES = [
#         ('Accepted', 'Accepted'),
#         ('Not Accepted', 'Not Accepted'),
#     ]
#     status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='Not Accepted')

#     def __str__(self):
#         return f"Reservation for {self.car} by {self.user}"
