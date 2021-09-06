import aiohttp
import asyncio
from time import time

loop = asyncio.get_event_loop()

def write_image(data):
    filename = 'file-{}.jpeg'.format(int(time()*1000))
    with open(filename, 'wb') as file:
        file.write(data)

async def fetchContent(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        write_image(data)

async def main():
    url = 'https://loremflickr.com/320/240'

    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = loop.create_task(fetchContent(url, session))
            tasks.append(task)
        
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    t0 = time()
    
    result = loop.run_until_complete(main())
    print(time() - t0)