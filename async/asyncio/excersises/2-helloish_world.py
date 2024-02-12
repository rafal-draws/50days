#!/bin/python3

import asyncio
import time

async def main():
    print(f"{time.ctime()} Hello!")
    await asyncio.sleep(1.0)
    print(f"{time.ctime()} Goodbye!")


loop = asyncio.get_event_loop()
''' 
You need a loop instance before you can run any couroutines.
Gives back the same loop instance each time, as long as you're using single thread. 

If inside async def function, you should call 
asyncio.get_running_loop()
'''

task = loop.create_task(main())
'''
task = loop.create_task(main())
task = loop.create_task(coro)

No execution until create task. create_task() schedules coroutine to be run on the loop.
The returned task object cna be used to monitor the status of the task (running|completed).
Can be canceled with task.cancel()
'''

loop.run_until_complete(task)
'''
This call will block the current thread, which will usually be main thread. Method run_until_complete(coro) will run until given coro completes, BUT ALL OTHER TASKS SCHEDULED ON THE LOOP WIL ALSO RUN WHILE THE LOOP IS RUNNING.
Internally, asyncio.run() calls run_until_complete() for you and therefore blocks the main thread in the same way.
'''

pending = asyncio.all_tasks(loop=loop)
for task in pending:
    task.cancel()


group = asyncio.gather(*pending, return_exceptions=True)
'''
group = asyncio.gather(task1, task2, task3)

When the "main" part of the program unblocks, either due to a PROCESS SIGNAL being received or the loop being stopped by some code calling loop.stop(), the code after run_until_complete() begins. 

.gather(coros) gathers the still-pending tasks, cancels them and will use loop.run_until_complete() again until these tasks are done.

.gather() is the method for doing the gathering.

asyncio.run() will do all of the cancelling, gathering, waiting for pending tasks to finish up
'''

loop.run_until_complete(group)

loop.close()

'''
loop.close() is usually the final action: it must be called on a stopped loop, and will clear all queues and shut down the executor. 

A stopped loop can be restartedm but a closed loop is gone forever.
asyncio.run will close the loop before returning. This is fine because run() creates a new event loop every time you call it.
'''
