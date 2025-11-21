from django.contrib import admin

from .models import Category, Product, ProductImage
from apps.reviews.models import Review

admin.site.register([Category, Product, ProductImage, Review])
