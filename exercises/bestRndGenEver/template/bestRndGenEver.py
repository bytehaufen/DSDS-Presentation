#!/usr/bin/env python3

import time


def bestRndGenEver() -> str:
    return f"{int(time.time()) % 64}"
