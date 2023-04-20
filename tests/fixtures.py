import pytest
from django.core.management import call_command


@pytest.fixture
def create_admin_user(django_user_model):
    """
    Return admin user
    """
    return django_user_model.objects.create_superuser(
        "admin", "abc@gmail.com", "password"
    )


@pytest.fixture(scope="session")
def db_fixture_setup(django_db_setup, django_db_blocker):
    """
    Load DB data fixture
    """
    with django_db_blocker.unblock():
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
