from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from django.http import HttpResponse
from elasticsearch_dsl import Q

from search.serializer import ProductInventorySerializer
from search.documents import ProductInventoryDocument


class SearchProductInventory(APIView, LimitOffsetPagination):
    productinventory_serializer = ProductInventorySerializer
    search_document = ProductInventoryDocument

    def get(self, request, query):
        try:
            q = Q(
                'multi_match',
                query=query,
                fields=[
                    'product.name'
                ], fuzziness='auto') & Q(
                    'bool',
                    should=[
                        Q('match', is_default=True),
                    ], minimum_should_match=1)

            search = self.search_document.search().query(q)
            search_result = search.execute()

            search_result = self.paginate_queryset(search_result, request, view=self)
            serializer = self.productinventory_serializer(search_result, many=True)
            return self.get_paginated_response(serializer.data)

        except Exception as e:
            return HttpResponse(e, status=500)
