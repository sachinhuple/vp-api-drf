from rest_framework.pagination import PageNumberPagination


class Paginate(PageNumberPagination):
    page_size = 5
    page_query_param = 'p'
    page_size_query_param = 'records'  # dynamically configures per page record : http://{url}/song/?p=1&records=10
    max_page_size = 10
    last_page_strings = 'end'
