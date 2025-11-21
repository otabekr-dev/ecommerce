from django.urls import path
from apps.reviews.views.review import ReviewListView, DetailedReviewList

from .views import (
    CategoryListView,
    CategoryDetailView,
    ProductListView,
    ProductDetailView,
    ProductImageListView,
    ProductImageDetailView,
    ProductSearchView,
)


urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/search/', ProductSearchView.as_view(), name='product-search'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('images/', ProductImageListView.as_view(), name='image-list'),
    path('images/<int:pk>/', ProductImageDetailView.as_view(), name='image-detail'),
    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', DetailedReviewList.as_view(), name='-detail'),
]
