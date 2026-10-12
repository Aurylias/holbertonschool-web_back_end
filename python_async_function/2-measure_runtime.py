#!/usr/bin/env python3
"""Place holder"""
import asyncio
from time import perf_counter

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Placeholder"""
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return (perf_counter() - start) / 5


if __name__ == "__main__":
    print(measure_time(3, 5))
    print(measure_time(4, 10))
    print(measure_time(5, 15))
