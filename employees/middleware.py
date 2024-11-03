from django.http import HttpResponse
from .models import BlackListedIPAddresses
from django.utils.deprecation import MiddlewareMixin

class GetIPAddressesMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        print(f"Client IP: {ip}")

class BlockIPAddress(MiddlewareMixin):
    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        if BlackListedIPAddresses.objects.filter(ip_address=ip).exists():
            return HttpResponse('You are blocked from this site', status=403)