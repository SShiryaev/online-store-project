from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from catalog.views import (ProductListView, ProductDetailView, ProductUpdateView,
                           ProductCreateView, ProductDeleteView, toggle_stock, FeedbackCreateView)

app_name = CatalogConfig.name

urlpatterns = [
    path('create/', never_cache(ProductCreateView.as_view()), name="create_product"),
    path('', ProductListView.as_view(), name='list_product'),
    path('contacts/', FeedbackCreateView.as_view(), name='contacts'),
    path('view/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name="view_product"),
    path('edit/<int:pk>/', never_cache(ProductUpdateView.as_view()), name="edit_product"),
    path('delete/<int:pk>/', never_cache(ProductDeleteView.as_view()), name="delete_product"),
    path('stock/<int:pk>/', toggle_stock, name="toggle_stock"),
]
