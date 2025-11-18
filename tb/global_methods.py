# alu/tb/global_methods.py
import os
import random
import cocotb
import logging
from collections import deque
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, ReadOnly, Timer

log = logging.getLogger("cocotb.tb")
level = os.getenv("LOG_LEVEL", "INFO").upper()
numeric_level = getattr(logging, level, logging.INFO)
log.setLevel(numeric_level)

if not log.handlers:
    handler = logging.StreamHandler()
    handler.setLevel(numeric_level)
    fmt = logging.Formatter("%(asctime)s %(levelname)-8s %(name)s - %(message)s", datefmt="%H:%M:%S")
    handler.setFormatter(fmt)
    log.addHandler(handler)
else:
    for h in log.handlers:
        h.setLevel(numeric_level)


def get_bit_field(value, msb, lsb):
    if msb < lsb:
        raise ValueError("MSB must be >= LSB")
    width = msb - lsb + 1
    mask = (1 << width) - 1
    return (value >> lsb) & mask


def set_bit_field(value, msb, lsb, new_value):
    if msb < lsb:
        raise ValueError("MSB must be >= LSB")
    width = msb - lsb + 1
    mask = ((1 << width) - 1) << lsb
    value &= ~mask
    value |= (new_value << lsb) & mask
    return value

