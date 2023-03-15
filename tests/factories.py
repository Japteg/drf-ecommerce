import factory
import pytest
from faker import Faker
from pytest_factoryboy import register
from inventory import models


fake = Faker()


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    name = factory.sequence(lambda n: "cat_name_%d" % n)
    slug = fake.lexify(text="cat_slug_??????")


register(CategoryFactory)