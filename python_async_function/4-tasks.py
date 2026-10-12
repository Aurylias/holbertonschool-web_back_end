"""Module like the task 1"""
import asyncio
from typing import List


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Calls wait_random n times and store results in a list then order it"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
