### Asyncio

"Asyncio provides another tool for concurrent programming in Python, that is more lightweight than threads or multiprocessing. In a very simple sense it does this by having an **event loop** execyte a collection of **tasks** with a key difference being that each tasks chooses **when to yield** control back to the event loop." - Philip Jones, medium.com

anything that is asynchronous - ***async*** keyword
awaiting something that is asynchronous from within something that is asynchronous - ***await*** keyword

Two groups of asyncio users:
- End-user developers
- Framework developers

# API summary

- Starting the **asyncio** event loop ***loop=asyncio.get_event_loop()***
- Calling **async**/**await** functions ***async def main():***
- Creating a *task* to be run on the loop ***loop.create_task(coro())*** 
- Waiting for multiple tasks to complete ***loop.run_until_complete*** 
- Closing the loop after all concurrent tasks have completed ***loop.close()***

# Blocking functions
3-blocking\_functions.py

# Tower of asyncio
1: Coroutines - async def, async with, async for, await
2: Event loop - asyncio.run(), BaseEventLoop
3: Futures - asyncio.Future
4: Tasks - asyncio.Task, asyncio.create\_task()
5: Subprocesses & threads - run\_in\_executor, asyncio.subprocess
6: Tools - asyncio.Queue
7: Network;transports - BaseTransport
8: Network;TCP&UDP - Protocol
9: Network;streams - StreamReader, StreamWriter, asyncio.open\_connection(), asyncio.start\_server()

important tiers:
Tier 1, Understanding how to write async def functions and use await to call and execute other coroutines is essential

Tier 2, Understanding how to start up, shut down and interact with the event loop is essential

Tier 5, Executors are necessary to use blocking code in your async application, and the reality is that most third-party libraries are not yet asyncio-compatible. A good example of this is the SQLAlchemy database ORM library, for which no feature-comperable alternative is available right now for asyncio.

Tier 6, If you need to feed data to one or more long-running coroutines, the best way to do that is with asyncio.Queue. This is exactly the same strategy as using queue.Queue for distributing data between threads. The asyncio version of Queue uses the same APi as the standard library queue module, bot uses coroutines instead of the blocking methods like get().

Tier 9, The sreams API give you the simplest way to handle socket communication over a network, and it is here that you should bein prototyping ideas for network applications. You may find that more fine-grained control is needed, and then you could swithc to the protocols API, but in most projects it's usually best to keep things simple until you know exactly what problem you're trying to solve.
