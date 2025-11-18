interface alu_interface #(parameter WIDTH = 8) (
    input bit clk,
    input bit rst_n
);
    // inputs
    logic [WIDTH-1:0] a_i;
    logic [WIDTH-1:0] b_i;
    logic [2:0] op_i;

    // outputs
    logic [WIDTH-1:0] result_o;
    logic zero_o;
    logic carry_o;
    logic error_o;
endinterface
