from concurrent.futures import ThreadPoolExecutor
import time
import random


def study():
    for i in range(10):
        print(f'studing {i}...')
        time.sleep(random.random())

def listen_to_music():
    for i in range(10):
        print(f'listening to music {i}...')
        time.sleep(random.random())

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(study)
        executor.submit(listen_to_music)

