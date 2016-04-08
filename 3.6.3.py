import requests

r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
while r.text.splitlines()[0].find('We') == -1:
        print(r.text)
        r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + r.text.splitlines()[0])
with open('result.txt', 'w') as file1:
    file1.write(r.text)


