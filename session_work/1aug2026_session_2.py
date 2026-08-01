import asyncio


async def send_data_db():
    print("Sending data to database...")
    await asyncio.sleep(50)
    print("Data sent to database!")   
    
async def my_workflow():
    print("Processing the data!")
    task = asyncio.create_task(send_data_db())
    print("Doing some other work while sending data to database...")
    await asyncio.sleep(3)
    print("User logged out!")
    

async def main():
    await(my_workflow())


asyncio.run(main())