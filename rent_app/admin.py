from django.contrib import admin
from .models import Property, Address, Gallery, Ameneties, PropertyDetails

class AddressInline(admin.StackedInline):  # Stack the address fields vertically
    model = Address
    extra = 1  # You can change this to allow more address forms

class GalleryInline(admin.TabularInline):  # Display gallery images in a tabular format
    model = Gallery
    extra = 1  # You can change this to allow more gallery forms

class AmenetiesInline(admin.StackedInline):  # Stack the amenities fields vertically
    model = Ameneties
    extra = 1  # You can change this to allow more amenities forms

class PropertyDetailsInline(admin.StackedInline):  # Stack the property details fields vertically
    model = PropertyDetails
    extra = 1  # You can change this to allow more property detail forms

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'property_type', 'added_by', 'created_at')  # Display property basic info in list view
    search_fields = ('title', 'property_type', 'added_by__username')  # Search properties by title, type, or added_by
    list_filter = ('property_type', 'created_at')  # Filter by type and date
    ordering = ('-created_at',)  # Order properties by creation date descending
    
    # Inline models
    inlines = [
        AddressInline,
        GalleryInline,
        AmenetiesInline,
        PropertyDetailsInline,
    ]

    # Optional: Add custom method to display the property details more nicely
    def rooms(self, obj):
        return obj.propertydetails.rooms if obj.propertydetails else 0
    rooms.short_description = 'Rooms'

    def kitchen(self, obj):
        return obj.propertydetails.kitchen if obj.propertydetails else 0
    kitchen.short_description = 'Kitchen'

    def bathroom(self, obj):
        return obj.propertydetails.bathroom if obj.propertydetails else 0
    bathroom.short_description = 'Bathroom'

# Register the Property model with the custom admin
admin.site.register(Property, PropertyAdmin)

# # Property Admin View
# class PropertyAdmin(admin.ModelAdmin):
#     list_display = ('title', 'property_type', 'added_by', 'created_at')  # Show title, type, user, timestamp
#     search_fields = ('title', 'property_type')
#     list_filter = ('property_type', 'added_by')  # Filters by property type and user
#     ordering = ('-created_at',)  # Order by created_at in descending order

# Address Admin View
class AddressAdmin(admin.ModelAdmin):
    list_display = ('property', 'street', 'city', 'state', 'zip_code', 'created_at')  # Show address and timestamp
    search_fields = ('property__title', 'city', 'state')  # Search by property title, city, and state
    list_filter = ('property__property_type', 'created_at')  # Filter by property type and timestamp
    ordering = ('-created_at',)  # Order by created_at in descending order

# Gallery Admin View
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('property', 'image', 'description', 'created_at')  # Show image description and timestamp
    search_fields = ('property__title', 'description')  # Search by property title and description
    list_filter = ('created_at',)  # Filter by timestamp
    ordering = ('-created_at',)  # Order by created_at in descending order

# Ameneties Admin View
class AmenetiesAdmin(admin.ModelAdmin):
    list_display = ('property', 'has_pool', 'has_gym', 'has_parking', 'created_at')  # Show amenities and timestamp
    search_fields = ('property__title',)  # Search by property title
    list_filter = ('created_at',)  # Filter by created_at
    ordering = ('-created_at',)  # Order by created_at in descending order

# PropertyDetails Admin View
class PropertyDetailsAdmin(admin.ModelAdmin):
    list_display = ('property', 'price', 'description', 'created_at')  # Show details and timestamp
    search_fields = ('property__title', 'description')  # Search by property title and description
    list_filter = ('created_at',)  # Filter by created_at
    ordering = ('-created_at',)  # Order by created_at in descending order

# Register models with the Django admin
# admin.site.register(Property, PropertyAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Ameneties, AmenetiesAdmin)
admin.site.register(PropertyDetails, PropertyDetailsAdmin)
