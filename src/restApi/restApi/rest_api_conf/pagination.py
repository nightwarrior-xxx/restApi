from rest_framework import pagination

class GlobalPaginationClass(pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 7
