import asyncio
import aiohttp
import yaml

from bs4 import BeautifulSoup

with open('cars.yml', 'r') as f:
    data = yaml.safe_load(f)


async def get_pages_count(session, manufacturer: str):
    print(f"starting calling: {manufacturer}") 
    
    async with session.get(data['urls']['base'] + manufacturer) as response:
        r  = await response.text()
        soup = BeautifulSoup(r, "html.parser")
        pages = soup.find_all("li", {"data-testid":"pagination-list-item"})[-1].find("span").text
        print("found ", pages, f" for {manufacturer}")


async def main():
    
    async with aiohttp.ClientSession() as session:
        tasks = [get_pages_count(session, manufacturer) for manufacturer in data['cars']]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
