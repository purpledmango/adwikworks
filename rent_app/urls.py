from django.urls import path
from . import views

urlpatterns=[
    path("", views.home_view, name="home"),
    path("properties", views.property_view, name="properties"),
    path("furnitures", views.furitures_view, name="furnitures"),
    path("about", views.about_view, name="about"),
    path("contact_us", views.contact_us, name="contact_us"),
    path("add_property", views.add_property, name="add_property"),
    path("add_property_detail/<int:property_id>/", views.add_property_details, name="add_property_detail"),
    path("add_images/<int:property_id>/", views.add_images, name="add_images"),
    path('profile/', views.user_profile, name='profile'),
    path('view_property/<int:property_id>/', views.view_property, name='view_property'),

]