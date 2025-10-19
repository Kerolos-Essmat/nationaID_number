import time
from django.utils.deprecation import MiddlewareMixin
from .models import APIAccessLog

class APILoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.start_time = time.time()
        print("Request started at:", request.start_time)

    def process_response(self, request, response):
        if hasattr(request, 'start_time'):
            execution_time = time.time() - request.start_time
        APIAccessLog.objects.create(
                request_path=request.path,
                user=request.user.username,
                ip_address=request.META.get('REMOTE_ADDR'),
                execution_time=execution_time,
                status_code=response.status_code
            )
        return response