#!/usr/bin/env python3
"""Module calculating the runtime for four asynchronously list comprehention"""
import asyncio
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_time():
    """Measure total runtime for four async_comprehension"""
    start = perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    return perf_counter() - start

if __name__ == "__main__":
    async def main():
        return await measure_time()

    print(asyncio.run(main()))
