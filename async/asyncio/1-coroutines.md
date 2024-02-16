# Coroutines

async functions are functions, not coroutines

```
>>>async def f():
...    return 123
...
>>>type(f)
<class 'funtion'>
>>>import inspect
>>>inspect.iscoroutinefunction(f)
True
```


Coroutine is initiated by "sending" it a None. This is done by event loop.

When coroutine *returns*, a special kind of exception is raised, called StopIteration. We can access the return value via .value attribute.
But from our point of view, the **async def** function will simply return a value with the return statement.
```
>>>async def f():
...   return 123
>>>coro = f()
>>>try:
...    coro.send(None)
...except StopIteration as E:
...    print('The answer was:', e.value)
...
The answer was: 123
```
await syntax awaits awaitable, therefore implementing __await__() or calling the result of async def fucntion is required

so we can perform following:

```
async def f():
    await asyncio.sleep(1.0)
    return 123

async def main():
    result = await f()
    return result
```

calling f() produces a coroutine, this means we are allowed to await it.


### Coroutine Exceptions

Coros can be fed with exceptions. This is most commonly used for cancellation.
When you call task.cancel(), the event loop will internally use coro.throw() to raise asyncio.CancelledError **inside** your coroutine.

```
coro = f()
coro.send(None)
coro.throw(Exception, 'blah')

# other way to inject an exception is to do it from the outside

async def f():
    try:
        while True: await asyncio.sleep(0)
    except asyncio.CancelledError:
        print('I was cancelled!')
    else:
        return 111

coro = f()
coro.send(None)
coro.send(None)
coro.throw(asyncio.CancelledError)
# Outputs : 
# I was cancelled!
# Traceback (most recent call last):
# file "<stdin>", line 1, in <module>
# StopIteration
```


## Event Loops

**Recomennded**
asyncio.get\_running\_loop() is callable from inside the context of a coroutine

it allows for coros to create more coros inside current event loop, without passing a loop instance through the functions


# Tasks and Futures

**Future is a supercall of Task** and it provide all of the functionality for the interaction with the loop.

**Future represents a future completion state of some activity and is managed by the loop.**
Task is exactly the same,** but the specific "activity" is a coroutine**, propably one of yours 
that **you created with an async def function plus create_task()**

**The Future class represents a *state* of something that is interacting with a loop**.

When a Future instance is created, the toggle is set to "not yet completed", but at some time later 
it will be "completed". In fact, a **Future** instance has a method called .done() that allows you to check the status.

```
from asyncio import Future
f = Future()
f.done()
# Outputs False
```

Future instance may also do the following:

- Have a "result" value set (use .set\_result(value) to set it and .result() to obtain it)
- Be cancelled with .cancel() (and check for cancellation with cancelled())
- Have additional callback functions added that will be run when the future completes

Even though Tasks are more common, you cant avoid Futures. 
For instance, running a function on an executor will return Future instance, not a Task.


Interaction with a Future instance:

```
import asyncio

async def main(f: asyncio.Future):
    await asyncio.sleep(1)
    f.set_result('I have finished.')

loop = asyncio.get\_event\_loop()
fut = asyncio.Future()
print(fut.done())
# prints False

loop.create\_task(main(fut))
loop.run\_until\_complete(fut)
# 'I have finished.'
print(fut.done())
# 'True'
print(fut.result())
#I have finished
```

You can either use asyncio.create\_task, or use asyncio.ensure\_future().




