from cocotb.triggers import RisingEdge


class Driver:
    def __init__(self, dut, clk):
        self.dut = dut
        self.clk = clk

    async def drive(self, txn):
        print(f'Driving transaction: \n{txn.print()}')
        self.req = txn
        self.dut.alu_intf.a_i.value = self.req.a
        self.dut.alu_intf.b_i.value = self.req.b
        self.dut.alu_intf.op_i.value = self.req.op
        await RisingEdge(self.clk)


