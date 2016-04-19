import requests
r = requests.get('http://127.0.0.1:8000/tomcatserv/furniture.jsp')
print(r.text)
