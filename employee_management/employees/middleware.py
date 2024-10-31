from django.http import HttpResponseForbidden

class BlockedIPMiddleware:
    BLOCKED_IPS = ['192.168.1.1', '10.0.0.2']

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.META.get('REMOTE_ADDR') in self.BLOCKED_IPS:
            return HttpResponseForbidden("Your IP address is blocked.")
        return self.get_response(request)