from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from lib.lib import get_national_id_info
# Create your views here.

def index(request):
    return JsonResponse({"message": "Welcome to the National ID Information API"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_national_id_info_api(request, national_id):
    info = get_national_id_info(national_id)
    if info:
        return JsonResponse(info)
    else:
        return JsonResponse({"error": "National ID not found"}, status=404)


