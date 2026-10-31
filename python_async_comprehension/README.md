# Python - Async Comprehension

This project covers asynchronous generators and comprehensions in Python.

## Tasks

| File | Description |
| ---- | ----------- |
| [0-async_generator.py](./0-async_generator.py) | Coroutine that loops 10 times, waits 1 second, and yields a random float between 0 and 10 |
| [1-async_comprehension.py](./1-async_comprehension.py) | Coroutine that collects 10 random numbers using an async comprehension over `async_generator` |
| [2-measure_runtime.py](./2-measure_runtime.py) | Coroutine that executes `async_comprehension` four times in parallel using `asyncio.gather` and measures total runtime |
