#!/usr/bin/env python3
"""Placeholder"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Place holder"""
    loop = asyncio.get_event_loop()
    return asyncio.creat_task(wait_random(max_delay))
