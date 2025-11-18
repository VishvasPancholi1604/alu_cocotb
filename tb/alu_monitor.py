import os
import sys

# current directory path
current_directory_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_directory_path)

from cocotb.triggers import RisingEdge
from alu_seq_item import ALUTransaction


class Monitor:
    def __init__(self, dut, clk):
        self.dut = dut
        self.clk = clk

    async def sample(self):
        print(f'Hii')
        while True:
            print(f'In while')
            await RisingEdge(self.clk)
            print(f'After rise edge')
            # await ReadOnly()
            txn = ALUTransaction()
            txn.a = int(self.dut.alu_intf.a_i.value)
            txn.b = int(self.dut.alu_intf.b_i.value)
            txn.op = int(self.dut.alu_intf.op_i.value)
            txn.result = int(self.dut.alu_intf.result_o.value)
            txn.zero = int(self.dut.alu_intf.zero_o.value)
            txn.carry = int(self.dut.alu_intf.carry_o.value)
            txn.error = int(self.dut.alu_intf.error_o.value)
            print(f'Monitor Sampled transaction:\n{txn.print()}')
