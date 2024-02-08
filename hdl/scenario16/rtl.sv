//---TOP MODULE FOR RTL DESIGN---//

module rtl #(parameter D_WIDTH = 6, A_WIDTH = 2, CREDIT_WIDTH = 3)
(
input                   clk,
input                   rst,
input  [(D_WIDTH-1):0]  up_data,
input                   up_valid,
output                  up_ready,
output [(D_WIDTH-1):0]  down_data,
output                  down_valid,
input                   down_ready
);

wire  [(D_WIDTH-1):0]         w_cbfc1_down_data;
wire                          w_cbfc1_down_valid;
wire                          w_fifocr1_up_ready;
wire                          w_fifocr1_up_credit;
wire  [(CREDIT_WIDTH-1):0]    w_cprm1_credit_initval_w;


custom_param #(.CREDIT_WIDTH (CREDIT_WIDTH))
CPRM1
(
         .credit_initval(w_cprm1_credit_initval_w));


credbasedfc_44 # (.D_WIDTH (D_WIDTH), .CREDIT_WIDTH (CREDIT_WIDTH))
CBFC1
(       .clk(clk),
        .rst(rst),
        .up_data(up_data),
        .up_valid(up_valid),
        .up_ready(up_ready),
        .down_data(w_cbfc1_down_data),
        .down_valid(w_cbfc1_down_valid),
        .down_credit(w_fifocr1_up_credit),
        .credit_initval(w_cprm1_credit_initval_w));

ff_fifo_credret_pow2_depth # (.D_WIDTH (D_WIDTH), .A_WIDTH (A_WIDTH))
FIFOCR1
(       .clk(clk),
        .rst(rst),
        .up_data(w_cbfc1_down_data),
        .up_valid(w_cbfc1_down_valid),
        .up_ready(w_fifocr1_up_ready),
        .up_credit(w_fifocr1_up_credit),
        .down_data(down_data),
        .down_valid(down_valid),
        .down_ready(down_ready));

endmodule
