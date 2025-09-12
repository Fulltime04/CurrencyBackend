from django.test import TestCase
import os
import requests
from django.http import JsonResponse

def get_crypto_data(request):
    api_key = os.getenv("API_KEY1")  # or API_KEY2 depending on what you need
    url = f"https://api.example.com/data?apikey={api_key}"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
# Create your tests here.
