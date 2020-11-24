import requests
from bs4 import BeautifulSoup

url = 'https://detik.com'
try:
    response = requests.get(url)
    if response.status_code==200:
        print(f'sukses{response}')
#        print(f'content: {response.text}')
        soup = BeautifulSoup(response.text, features="html.parser")
        print(f'hasil pemanggilan {url}')
        print(f'title: {soup.title.string}')
    else:
        print(f'status error: {response.status_code}')
except Exception as e:
#    print(f'status error:{response.status_code}')
    print(f'There is error: {e}')
print('program ended')
