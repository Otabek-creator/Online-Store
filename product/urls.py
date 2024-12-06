from django.urls import path

from .views import (
    AboutView,
    ProductCreateView,
    ProductListView,
    ProductDetailView,
    ProductUpdateView,
    ProductDeleteView,
    BucketProductListView,
    BucketProductCreateView,
    BucketProductDeleteView,
    RatingCreateView,
    CategoryListCreate,
    ProductListCreate, ContactListCreate, BucketListCreate, BucketProductListCreate, RatingListCreate,

)

urlpatterns = [
    path('list/', ProductListView.as_view(), name='product_list'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('about/', AboutView.as_view(), name='about'),

    path('bucket/', BucketProductListView.as_view(), name='bucket'),
    path('bucket/product/create/<int:product_id>', BucketProductCreateView.as_view(), name='bucket_product_create'),
    path('bucket/product/delete/<int:product_id>', BucketProductDeleteView.as_view(), name='bucket_product_delete'),

    path('rating/create/<int:product_id>', RatingCreateView.as_view(), name='rating_create'),

    path('api/categories/', CategoryListCreate.as_view(), name='category-list-create'),
    path('api/products/', ProductListCreate.as_view(), name='product-list-create'),
    path('api/contacts/', ContactListCreate.as_view(), name='contact-list-create'),
    path('api/buckets/', BucketListCreate.as_view(), name='bucket-list-create'),
    path('api/bucket-products/', BucketProductListCreate.as_view(), name='bucket-product-list-create'),
    path('api/ratings/', RatingListCreate.as_view(), name='rating-list-create'),
]
