import os
import requests
from django.http import JsonResponse

# Fixer.io symbols endpoint
def get_symbols(request):
    api_key = os.getenv("API_KEY1")
    url = f"https://data.fixer.io/api/symbols?access_key={api_key}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

# Exchange rate conversion
def convert_currency(request):
    from_currency = request.GET.get("from")
    to_currency = request.GET.get("to")
    amount = request.GET.get("amount")

    api_key = os.getenv("API_KEY2")  # API_KEY2 for exchangerate-api.com
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}/{amount}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return JsonResponse(response.json())
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

