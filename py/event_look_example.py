import asyncio

async def long_running_task():
    print("long running task started")
    await asyncio.sleep(10)
    print("long running task completed")



my_evt_loop = asyncio.get_event_loop()
#my_evt_loop.create_task(long_running_task())
try:
    my_evt_loop.run_until_complete(long_running_task())

finally:
    my_evt_loop.close()