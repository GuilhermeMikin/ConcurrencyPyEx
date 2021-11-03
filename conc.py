import asyncio

async def my_coroutine():
    return "hello"


c = my_coroutine()
# print(c)
loop = asyncio.get_event_loop()
r = loop.run_until_complete(c)
print(r)