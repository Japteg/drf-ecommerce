from django.urls import path
from search.views import SearchProductInventory

urlpatterns = [
    path('<str:query>', SearchProductInventory.as_view())
]
