from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        call_command("makemigrations")
        call_command("migrate")
        call_command("loaddata", "db_admin_fixture.json")
        call_command("loaddata", "db_category_fixtures.json")
        call_command("loaddata", "db_product_fixtures.json")
        call_command("loaddata", "db_type_fixtures.json")
        call_command("loaddata", "db_brand_fixtures.json")
        call_command("loaddata", "db_product_inventory_fixtures.json")
        call_command("loaddata", "db_media_fixtures.json")
        call_command("loaddata", "db_stock_fixtures.json")
        call_command("loaddata", "db_product_attribute_fixtures.json")
        call_command("loaddata", "db_product_attribute_value_fixtures.json")
        call_command("loaddata", "db_product_attribute_values_fixtures.json")
        call_command("loaddata", "db_category_product_fixtures.json")
        call_command("loaddata", "db_product_type_attribute_fixtures.json")
