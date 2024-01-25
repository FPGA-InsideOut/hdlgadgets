//---TOP MODULE FOR RTL DESIGN---//

module rtl #(parameter D_WIDTH = 6, parameter A_WIDTH = 2)
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

wire  [D_WIDTH - 1:0] w_sftreg1_down_data;
wire                  w_sftreg1_down_valid;
wire                  w_clgk1_up_ready;
wire  [D_WIDTH - 1:0] w_clgk1_down_data;
wire                  w_clgk1_down_valid;
wire                  w_fifo2_up_ready;

shiftreg_4depth # (.D_WIDTH (D_WIDTH))
SFTREG1
(       .clk(clk),
        .rst(rst),
        .up_data(up_data),
        .up_valid(up_valid),
        .up_ready(up_ready),
        .down_data(w_sftreg1_down_data),
        .down_valid(w_sftreg1_down_valid),
        .down_ready(w_clgk1_up_ready));

custom_logic # (.D_WIDTH (D_WIDTH))
CLGC1
(       .clk(clk),
        .rst(rst),
        .up_data(w_sftreg1_down_data),
        .up_valid(w_sftreg1_down_valid),
        .up_ready(w_clgk1_up_ready),
        .down_data(w_clgk1_down_data),
        .down_valid(w_clgk1_down_valid),
        .down_ready(w_fifo2_up_ready));

ff_fifo_pow2_depth # (.D_WIDTH (D_WIDTH), .A_WIDTH (A_WIDTH))
FIFO2
(       .clk(clk),
        .rst(rst),
        .up_data(w_clgk1_down_data),
        .up_valid(w_clgk1_down_valid),
        .up_ready(w_fifo2_up_ready),
        .down_data(down_data),
        .down_valid(down_valid),
        .down_ready(down_ready));

endmodule
