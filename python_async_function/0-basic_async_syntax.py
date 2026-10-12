#!/usr/bin/env python3
"""Module for wating a random amount of time asynchronously"""
import asyncio
from random import uniform

async def wait_random(max_delay: int =10) -> float:
    """Wait for a random amount of time from 0 to max_delay"""
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

if __name__ == "__main__":
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
