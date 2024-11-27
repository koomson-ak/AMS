from django.urls import path
from django.contrib.auth import views
from . import views
from .views import (
    AssetListView,
    AssetDeleteView,
    AssetCreateView,
    AssetUpdateView,
    AssetDetailView,
)

urlpatterns = [
    path('', AssetListView.as_view(), name='asset_list'),
    path('<int:pk/', AssetDetailView.as_view(), name='asset_detail'),
    path('new/', AssetCreateView.as_view(), name='asset_create'),
    path('<int:pk/edit', AssetUpdateView.as_view(), name='asset_update'),
    path('<int:pk>/delete', AssetDeleteView.as_view(), name='asset_delete'),
]