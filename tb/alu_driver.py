from cocotb.triggers import RisingEdge
from cocotb.queue import Queue

class Driver:
    def __init__(self, dut, clk):
        self.dut = dut
        self.clk = clk
        self.req_queue = Queue()

    async def push(self, req):
        await self.req_queue.put(req)

    async def single_drive(self, txn):
        print(f'Driving transaction: \n{txn.print()}')
        self.dut.alu_intf.a_i.value = txn.a
        self.dut.alu_intf.b_i.value = txn.b
        self.dut.alu_intf.op_i.value = txn.op
        await RisingEdge(self.clk)

    async def drive(self):
        while True:
            txn = await self.req_queue.get()
            await self.single_drive(txn)

