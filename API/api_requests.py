""" 
Requests library - HTTP requests
BeautifulSoup - To parse information from requests

VEDIOS TO WATCH
1) BeautifulSoup of coreyScafer


"""
import requests

r = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(r.text)
img = requests.get("https://image-placeholder.net/img/600x400.jpg")
print(img.content)

with open ('img.png','wb') as f:
    f.write(img.content) 

payload = {'count':25,'page' :2 }
p = requests.get("https://httpbin.org/get", params = payload)
print(p.text)

payload = {'name':'sri','id':20}
p = requests.post("https://httpbin.org/post", data = payload)
res = p.json()
print(res['form']) 

""" Basic authentication """

a = requests.get("https://httpbin.org/basic-auth/sri/pass", auth=('sri','pass'))
print(a.text)
