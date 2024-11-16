from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Property, PropertyDetails, Gallery, Ameneties, Address


def home_view(request):
    properties = Property.objects.all()[::-1]
    return render(request, "index.html", {'properties':properties})

def property_view(request):
    properties = Property.objects.all()[::-1]
    return render(request, "properties.html", {'properties':properties})

def furitures_view(request):
    return render(request, "furnitures.html")

def about_view(request):
    return render(request, "about.html")

def contact_us(request):
    return render(request, "contactus.html")

def add_property(request):
    if request.method == "POST":
        # Get form data
        property_name = request.POST.get('property_name')
        property_type = request.POST.get('property_type')
        user = request.user

        # Validate the input
        if not property_name or not property_type:
            messages.error(request, "All fields are required!")
            return redirect('add_property')

        # Save the listing
        newProperty = Property.objects.create(
            added_by=user,
            title=property_name,
            property_type=property_type
        )

        messages.success(request, "Property added successfully!")
        return redirect('add_property_detail', property_id=newProperty.id)  

    # Render the form
    return render(request, 'add_property.html')


def add_property_details(request, property_id):
    property = get_object_or_404(Property, id=property_id)

    if request.method == 'POST':
        # Get data from the request
        property_name = request.POST.get('property_name')
        property_type = request.POST.get('property_type')
        description = request.POST.get('description')
        area = request.POST.get('area')
        rooms = request.POST.get('rooms')
        kitchen = request.POST.get('kitchen')
        bathroom = request.POST.get('bathroom')
        price = request.POST.get('price')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        images = request.FILES.getlist('images')  # Handle image uploads
        has_pool = request.POST.get('has_pool')
        has_gym = request.POST.get('has_gym')
        has_parking = request.POST.get('has_parking')

        # Save PropertyDetails
        property_details = PropertyDetails.objects.create(
            property=property,
            description=description,
            area=area,
            price=price,
            rooms=rooms,
            kitchen=kitchen,
            bathroom=bathroom
        )

        # Save Address
        address = Address.objects.create(
            property=property,
            street=street,
            city=city,
            state=state,
            zip_code=zip_code,
        )

        # Save Amenities
        amenities = Ameneties.objects.create(
            property=property,
            has_pool=has_pool == 'on',
            has_gym=has_gym == 'on',
            has_parking=has_parking == 'on',
        )

        # Redirect to the property details page
        return redirect('add_images', property_id=property.id)

    return render(request, 'add_property_details.html', {'property': property})

def add_images(request, property_id):
    property_instance = get_object_or_404(Property, id=property_id)

    if request.method == "POST":
        # Handle image upload
        image = request.FILES.get('image')
        description = request.POST.get('description', '')

        if image:
            Gallery.objects.create(property=property_instance, image=image, description=description)
            messages.success(request, "Image uploaded successfully!")
        else:
            messages.error(request, "Please select an image to upload.")

        return redirect('add_images', property_id=property_id)

    # Retrieve gallery images for the property
    gallery_images = Gallery.objects.filter(property=property_instance)

    context = {
        'property': property_instance,
        'gallery': gallery_images
    }
    return render(request, 'add_property_images.html', context)


def user_profile(request):
    return render(request, "profile.html")

def view_property(request, property_id):
    # Fetch the property using the provided ID
    property = get_object_or_404(Property, id=property_id)
    
    # You can access the related models like propertydetails, gallery, etc. through the property instance
    
    return render(request, 'view_property.html', {'property': property})