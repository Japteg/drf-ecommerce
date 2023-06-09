from django.urls import include, path
from rest_framework import routers

from drf import views

router = routers.DefaultRouter()
router.register(
    r"category/(?P<slug>[^/.]+)", views.ProductByCategory, basename="productbycategory",
)
router.register(r"item/(?P<id>[^/.]+)", views.SingleProductViewSet, basename="items")


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
]
