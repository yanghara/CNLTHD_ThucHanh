from rest_framework import pagination


class ItemPaginaiton(pagination.PageNumberPagination):
    page_size = 2
