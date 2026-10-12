#!/usr/bin/env python3
"""Placeholder"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """"""
    numbers = [i async for i in async_generator()]
    return numbers

if __name__ == "__main__":
    async def main():
        print(await async_comprehension())

    asyncio.run(main())
