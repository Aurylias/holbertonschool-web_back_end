#!/usr/bin/env python3
"""Module for generating random float each seconds"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yield a random float between 0 and 10 each seconds"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
