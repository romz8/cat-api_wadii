import requests

url=' https://api.thecatapi.com/v1/images/888'
headers={'x-api-key':'1a2f393f-7085-44b4-a1ff-9d06dba99730'}

r=requests.get(url,headers=headers)
image=r.json()

print(image['url'])