from django.utils.deprecation import MiddlewareMixin
from djangorestframework_camel_case.util import underscoreize


class CamelCaseQueryParamsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.method == 'GET':
            request.GET = request.GET.copy()
            transformed = underscoreize(request.GET)
            request.GET.clear()
            request.GET.update(transformed)
