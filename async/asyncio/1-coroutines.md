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
