import os
import sys

# current directory path
current_directory_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_directory_path)

from global_methods import *
from alu_seq_item import ALUTransaction
from alu_driver import Driver
from alu_monitor import Monitor
from cocotb.triggers import Timer

@cocotb.test()
async def alu_sanity_test(dut):
    try:
        width = len(dut.alu_dut.a_i)
        print(f'found width: {width}')
    except Exception:
        width = 8
        print(f'could not find width, default is 8')

    txn_h = ALUTransaction(a=7,b=3,op=1)
    alu_driver = Driver(dut, dut.clk)
    monitor = Monitor(dut, dut.clk)
    mon_task = cocotb.start_soon(monitor.sample())
    await alu_driver.drive(txn_h)
    print(f'output: {int(dut.alu_intf.result_o.value)}')
    await Timer(10, unit="ns")
    #print(txn_h.print())
