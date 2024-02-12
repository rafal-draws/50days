#!/bin/python3
import time
import asyncio

async def main():
    print(f'{time.ctime()} hello')
    await asyncio.sleep(1.0)
    print(f'{time.ctime()} goodbye')

def blocking():
    time.sleep(0.5)
    print(f'{time.ctime()} hello from a thread!')

loop = asyncio.get_event_loop()
task = loop.create_task(main())

loop.run_in_executor(None, blocking)
loop.run_until_complete(task)

pending = asyncio.all_tasks(loop=loop)
for task in pending:
    task.cancel()

group = asyncio.gather(*pending, return_exceptions=True)
loop.run_until_complete(group)
loop.close()

'''
def blocking() 
calls a time.sleep() which is INTERNAL function, running on main thread, which would prevent the event loop from running. cannot be called anywhere in the main thread, especially since asyncio loop is there.

await loop.run_in_executor(None, func)
Sometimes you need to run things in a separate thread or even a separate process: this method is used for exactly that. 
Here we pass our blocking function to be run in the default executor. 
Note that run_in_executor DOES NOT BLOCK the main thread. 

It only schedules the executor task to run (it returns a Future, which means you can await it if the method is called within another coroutine function). 
The executor task will begin executing only after run_until_complete() is called, which allows the event loop to start processing events.

'''
