import os
from dotenv import load_dotenv

load_dotenv()

api_key_1 = os.getenv("API_KEY1")
api_key_2 = os.getenv("API_KEY2")

print("API_KEY1:", api_key_1)
print("API_KEY2:", api_key_2)