# Python - Async

This project covers asynchronous programming in Python using `asyncio`.

## Tasks

| File | Description |
| ---- | ----------- |
| [0-basic_async_syntax.py](./0-basic_async_syntax.py) | Asynchronous coroutine that waits for a random delay between 0 and `max_delay` seconds and returns it |
| [1-concurrent_coroutines.py](./1-concurrent_coroutines.py) | Async routine that executes multiple coroutines concurrently and returns delays in ascending order |
| [2-measure_runtime.py](./2-measure_runtime.py) | Function that measures the runtime of `wait_n` and returns the average time per task |
| [3-tasks.py](./3-tasks.py) | Regular function returning an `asyncio.Task` for `wait_random` |
| [4-tasks.py](./4-tasks.py) | Async routine that uses `task_wait_random` to spawn multiple tasks concurrently |
