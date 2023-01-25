import time
import requests
from threading import Thread

def get_html(link):
    time.sleep(1)
    res = requests.get('https://ya.ru')
    if res:
        print('Response OK')
    else:
        print('Response Failed')

start = time.time()

for i in range(5):
    get_html(i+1)

print('Время работы: {:1f}'.format(time.time()-start))

start = time.time()
threads = [Thread(target=get_html, args=(i+1, )) for i in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print('Время работы: {:1f}'.format(time.time()-start))