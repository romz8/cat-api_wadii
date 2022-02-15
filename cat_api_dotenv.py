import requests
from dotenv import load_dotenv
import os

#get environment variable (in our case the api key)
load_dotenv()
API_KEY = os.getenv("API_KEY")

url = 'https://api.thecatapi.com/v1/images/888'
headers = {'x-api-key':API_KEY}

r =  requests.get(url,headers=headers)
image = r.json()

print(image['url'])