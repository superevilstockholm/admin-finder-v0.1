import aiohttp
import asyncio
import json
import random
from functools import wraps

def url_validator(func):
    @wraps(func)
    def wrapper(self, url: str, *args, **kwargs):
        if not (url.startswith("http://") or url.startswith("https://")):
            url = "http://" + url
        if not url.endswith("/"):
            url += "/"
        return func(self, url, *args, **kwargs)
    return wrapper

class AdminFinder():
    def __init__(self) -> None:
        with open(file='useragent.json', mode='r') as file:
            self.useragents = json.load(file)
        self.headers = {
            'User-Agent': random.choice(self.useragents)['useragent']
        }

    def _changeUserAgent(self) -> None:
        self.headers['User-Agent'] = random.choice(self.useragents)['useragent']

    @url_validator
    async def finder(self, url: str) -> None:
        berhasil = []
        with open(file='adminFinder.txt', mode='r', encoding='utf-8') as file:
            wordlist = file.read().splitlines()
        tasks = []
        async with aiohttp.ClientSession() as session:
            for word in wordlist:
                tasks.append(self.check_url(session, url + word))
            results = await asyncio.gather(*tasks)
            for result in results:
                if result:
                    berhasil.append(result)
        print("\033[0;32mUrl yang berhasil:", berhasil,"\033[0;37m")

    async def check_url(self, session: aiohttp.ClientSession, full_url: str):
        try:
            timeout = aiohttp.ClientTimeout(
                sock_connect=10,
            )
            async with session.head(full_url, headers=self.headers, timeout=timeout) as response:
                if response.status == 200:
                    print(f"\033[0;32mFound [200]: {full_url}\033[0;37m")
                    return full_url
                elif response.status == 404:
                    print(f"\033[0;31mNot Found [404]: {full_url}\033[0;37m")
                elif response.status == 403:
                    print(f"\033[0;31mForbidden [403]: {full_url}\033[0;37m")
                    self._changeUserAgent()
                elif response.status == 500:
                    print(f"\033[0;31mInternal Server Error [500]: {full_url}\033[0;37m")
                    self._changeUserAgent()
                elif response.status == 503:
                    print(f"\033[0;31mService Unavailable [503]: {full_url}\033[0;37m")
                    self._changeUserAgent()
                else:
                    print(f"\033[0;31mUnknown Status [{response.status}]: {full_url}\033[0;37m")
        except Exception as e:
            print(f"Error accessing {full_url}: {e}")
        return None

async def main():
    finder = AdminFinder()
    await finder.finder(str(input("Insert URL: ")))

if __name__ == "__main__":
    asyncio.run(main())