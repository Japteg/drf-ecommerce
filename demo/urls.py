from django.urls import path, re_path

from . import views

app_name = "demo"

urlpatterns = [
    path("", views.home, name="home"),
    path("categories/", views.category),
    path("product-by-category/<slug:category>/", views.product_by_category,
         name="product_by_category"),
    path("<slug>", views.product_detail, name="product_detail"),
]
