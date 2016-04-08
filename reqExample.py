import requests
r = requests.get('http://127.0.0.1:8000/tomcatserv/furniture.jsp')
print(r.status_code)
print(r.encoding)
print(r.headers)
print(r.url)
print(r.elapsed)
print(r.text)