from rest_framework import serializers
from inventory.models import ProductInventory, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name"]
        read_only = True
        editable = False


# These serializer fields should match with what is defined in document
class ProductInventorySerializer(serializers.ModelSerializer):

    product = ProductSerializer(many=False, read_only=True)

    class Meta:
        model = ProductInventory
        fields = [
            "id",
            "sku",
            "store_price",
            "is_default",
            "product"
        ]
