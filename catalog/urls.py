from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductListView, ProductDetailView, ProductUpdateView, ProductCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('create/', ProductCreateView.as_view(), name="create"),
    path('', ProductListView.as_view(), name='list'),
    path('contacts/', contacts, name='contacts'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name="view"),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name="edit"),
]
