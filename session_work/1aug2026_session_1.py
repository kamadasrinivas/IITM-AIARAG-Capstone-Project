import asyncio


async def hello():
    print("Hello, world!")
    await asyncio.sleep(1)
    print("Hello again!")   
    
async def howru():
    print("Howru!")
    await asyncio.sleep(1)
    print("howru again!")
    
async def fine():
    print("fine!")
    await asyncio.sleep(1)
    print("fine again!")


async def main():
    await asyncio.gather(hello(), howru(), fine())


asyncio.run(main())