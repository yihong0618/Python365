import asyncio
import aiohttp
import uvloop

URL = "http://127.0.0.1:8000/{}"
words = ["Hello", "Python", "Fans", "!"]


async def getPage(session, word):
    with aiohttp.Timeout(10):
        async with session.get(URL.format(word)) as resp:
            print(await resp.text())


loop = uvloop.new_event_loop()
asyncio.set_event_loop(loop)
session = aiohttp.ClientSession(loop=loop)

tasks = []
for word in words:
    tasks.append(getPage(session, word))

loop.run_until_complete(asyncio.gather(*tasks))

loop.close()
session.close()
