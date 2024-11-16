from django.db import models
from auth_app.models import CustomUser

property_choices = [
    ('Rent', "Rent"),
    ('Sell', "Sell"),
]

class Property(models.Model):
    title = models.CharField(max_length=300, verbose_name="Ad Name")
    property_type = models.CharField(max_length=4, choices=property_choices)
     
    added_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)  # Timestamp for creation

    def __str__(self):
        return self.title  # You can return any field that best represents the Property model

class Address(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)  # Timestamp for creation

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.zip_code}"

class Gallery(models.Model):
    property = models.ForeignKey(Property, related_name='gallery', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/gallery_images/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)  # Timestamp for creation

    def __str__(self):
        return f"Image for {self.property.title} - {self.description[:30]}"  # Truncating description for a concise output

class Ameneties(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE)
    has_pool = models.BooleanField(default=False)
    has_gym = models.BooleanField(default=False)
    has_parking = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)  # Timestamp for creation

    def __str__(self):
        amenities = []
        if self.has_pool:
            amenities.append("Pool")
        if self.has_gym:
            amenities.append("Gym")
        if self.has_parking:
            amenities.append("Parking")
        return f"Amenities for {self.property.title}: {', '.join(amenities) if amenities else 'No amenities'}"

class PropertyDetails(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    area=models.IntegerField(null=True, blank=True) 
    rooms = models.IntegerField(null=True, blank=True) 
    kitchen = models.IntegerField( null=True, blank=True)
    bathroom = models.IntegerField( null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True) 

    def __str__(self):
        return f"Details for {self.property.title}: {self.price} - {self.description[:30]}"  # Truncating description
