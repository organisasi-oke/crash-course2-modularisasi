import requests

url = 'https://de tik.com'
try:
    response = requests.get(url)
    if response.status_code==200:
        print(f'sukses{response}')
        print(f'content: {response.text}')
    else:
        print(f'status error: {response.status_code}')
except Exception as e:
#    print(f'status error:{response.status_code}')
    print(f'There is error: {e}')
print('program ended')
