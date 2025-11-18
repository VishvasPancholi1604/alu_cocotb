module alu #(
    parameter WIDTH = 8
)(
    input  logic                clk,
    input  logic                rst_n,
    input  logic [WIDTH-1:0]    a_i,
    input  logic [WIDTH-1:0]    b_i,
    input  logic [2:0]          op_i,      // 3-bit operation select

    output logic [WIDTH-1:0]    result_o,
    output logic                zero_o,
    output logic                carry_o,
    output logic                error_o
);

    typedef enum logic [2:0] {
        OP_ADD = 3'b000,
        OP_SUB = 3'b001,
        OP_AND = 3'b010,
        OP_OR  = 3'b011,
        OP_XOR = 3'b100,
        OP_SHL = 3'b101,
        OP_SHR = 3'b110,
        OP_CMP = 3'b111
    } alu_op_e;

    logic [WIDTH:0] add_sub_result;

    always_comb begin
        result_o = '0;
        carry_o  = 1'b0;
        error_o  = 1'b0;

        case (op_i)
            OP_ADD: begin
                add_sub_result = a_i + b_i;
                result_o = add_sub_result[WIDTH-1:0];
                carry_o  = add_sub_result[WIDTH];
            end
            OP_SUB: begin
                add_sub_result = a_i - b_i;
                result_o = add_sub_result[WIDTH-1:0];
                carry_o  = add_sub_result[WIDTH]; // borrow
            end
            OP_AND: result_o = a_i & b_i;
            OP_OR : result_o = a_i | b_i;
            OP_XOR: result_o = a_i ^ b_i;
            OP_SHL: result_o = a_i << 1;
            OP_SHR: result_o = a_i >> 1;
            OP_CMP: begin
                result_o = (a_i == b_i);
            end
            default: begin
                result_o = '0;
                error_o  = 1'b1;
            end
        endcase
    end

    always_ff @(posedge clk or negedge rst_n) begin
        if(!rst_n) begin
            zero_o <= 1'b0;
        end
        else begin
            zero_o <= (result_o == '0);
        end
    end
endmodule

