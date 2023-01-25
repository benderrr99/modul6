import time
from threading import Thread

def get_thread(thread_name):
    time.sleep(1)
    print(f'Поток № {thread_name} запущен')

start = time.time()

for i in range(5):
    get_thread(i+1)
print('Время работы: {:1f}'.format(time.time()-start))

start = time.time()
threads = [Thread(target=get_thread, args=(i+1, )) for i in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print('Время работы: {:1f}'.format(time.time()-start))