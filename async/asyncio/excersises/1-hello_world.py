#!/bin/python3

import asyncio, time


async def main():
    print(f"{time.ctime()} Hello!")
    await asyncio.sleep(1.0)
    print(f"{time.ctime()} Goodbye!")


asyncio.run(main()) # asyncio provides a run() function to execute an async def function and all other couroutines called from there, like sleep() in line 8 in the main() function
