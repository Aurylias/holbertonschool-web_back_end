#!/usr/bin/env python3
"""Module for creating task asynchronously"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create tasks"""
    loop = asyncio.get_event_loop()
    return asyncio.create_task(wait_random(max_delay))
