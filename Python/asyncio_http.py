import socket
from urllib.parse import urlparse
import asyncio

async def get_url(url):
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"
        
    al_lines = []
    reader, writer = await asyncio.open_connection(host,80)
    writer.write("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))

    async for raw_line in reader:
        data = raw_line.decode("utf8")
        al_lines.append(data)

    html = "\n".join(al_lines)
    return html


async def main():
    tasks = []
    for url in range(20):
        url = "https://www.baidu.com"
        tasks.append(asyncio.ensure_future(get_url(url)))    
    for task in asyncio.as_completed(tasks):
        result = await task
        print(result)

if __name__ == "__main__": 
    import time
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print('last time:{}'.format(time.time() - start_time))
