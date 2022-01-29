import requests
import sys

url=' https://api.thecatapi.com/v1/images/888'
headers={'x-api-key':sys.argv[1]}

r=requests.get(url,headers=headers)
image=r.json()

print(image['url'])