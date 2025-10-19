from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from lib.lib import get_national_id_info
# Create your views here.

def index(request):
    return JsonResponse({"message": "Welcome to the National ID Information API"})

def get_national_id_info(request, national_id):
    info = get_national_id_info(national_id)
    if info:
        return JsonResponse(info)
    else:
        return JsonResponse({"error": "National ID not found"}, status=404)


