from django.urls import path
from django.views.decorators.cache import never_cache

from materials.apps import MaterialsConfig
from materials.views import (MaterialCreateView, MaterialListView, MaterialDetailView,
                             MaterialUpdateView, MaterialDeleteView)

app_name = MaterialsConfig.name

urlpatterns = [
    path('create/', never_cache(MaterialCreateView.as_view()), name="create"),
    path('', MaterialListView.as_view(), name="list"),
    path('view/<int:pk>/', MaterialDetailView.as_view(), name="view"),
    path('edit/<int:pk>/', never_cache(MaterialUpdateView.as_view()), name="edit"),
    path('delete/<int:pk>/', never_cache(MaterialDeleteView.as_view()), name="delete"),
]
