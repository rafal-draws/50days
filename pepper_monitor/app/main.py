import asyncio
import aiohttp

import yaml

from aiohttp import ClientSession
from bs4 import BeautifulSoup


def get_data():
    try:
        with open('conf/config.yml', 'r') as f:
            data = yaml.safe_load(f)
        return data
    except Exception as e:
        print(f"Config file couldn't be read. \nException: {e}")

async def fetch_pepper_url(url: str, session: ClientSession, **kwargs) -> str:
    resp = await session.request("GET", url=url, **kwargs)
    html = await resp.text()
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.find('title').text)
    



async def crawl(urls: list, **kwargs) -> None:
    async with ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(
                    fetch_pepper_url(url=url,session=session)
                    )
            await asyncio.gather(*tasks)

def main():
    data = get_data()

    orders = [_ for _ in data['orders']]
    urls = [f"https://www.pepper.pl/grupa/{order['group']['name']}-{order['group']['sort']}" for order in orders]
    asyncio.run(crawl(urls=urls))
    



if __name__ == "__main__":
    import time
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    
    print(f"Time elapsed for {__file__} was {elapsed}")
