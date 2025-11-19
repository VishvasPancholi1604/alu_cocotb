// `include "alu_interface.sv"
// `include "alu.sv"

module top;
    bit clk, rst_n;
    always #5 clk = ~clk;

    // ALU design under test
    alu alu_dut(
        .clk(clk),
        .rst_n(rst_n),
        .a_i(alu_intf.a_i),
        .b_i(alu_intf.b_i),
        .op_i(alu_intf.op_i),
        .result_o(alu_intf.result_o),
        .zero_o(alu_intf.zero_o),
        .carry_o(alu_intf.carry_o),
        .error_o(alu_intf.error_o)
    );

    // ALU interface
    alu_interface alu_intf(
        .clk(clk),
        .rst_n(rst_n)
    );

    initial
    begin
        rst_n = 1;
        #1; rst_n = 0;
        #5 rst_n = 1;
    end

    initial
    begin
`ifdef COCOTB_SIM
        $dumpfile("dump.vcd");
        $dumpvars(0, top);
`endif
        #100; $finish();
    end

endmodule
