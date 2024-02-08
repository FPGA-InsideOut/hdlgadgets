//---TOP MODULE FOR RTL DESIGN---//

module rtl #(parameter D_WIDTH = 6, parameter A_WIDTH = 2)
(
input                   clk,
input                   rst,
input  [(D_WIDTH-1):0]  up_data,
input                   up_valid,
output                  up_ready,
output [(D_WIDTH-1):0]  down_data_a,
output                  down_valid_a,
input                   down_ready_a,
output [(D_WIDTH-1):0]  down_data_b,
output                  down_valid_b,
input                   down_ready_b
);

wire  [(D_WIDTH-1):0] w_fifo1_down_data;
wire                  w_fifo1_down_valid;
wire                  w_clgk1_up_ready;
wire  [(D_WIDTH-1):0] w_clgk1_down_data_a;
wire                  w_clgk1_down_valid_a;
wire                  w_fifo2_up_ready;
wire  [(D_WIDTH-1):0] w_clgk1_down_data_b;
wire                  w_clgk1_down_valid_b;
wire                  w_fifo3_up_ready;

ff_fifo_pow2_depth # (.D_WIDTH (D_WIDTH), .A_WIDTH (A_WIDTH))
FIFO1
(       .clk(clk),
        .rst(rst),
        .up_data(up_data),
        .up_valid(up_valid),
        .up_ready(up_ready),
        .down_data(w_fifo1_down_data),
        .down_valid(w_fifo1_down_valid),
        .down_ready(w_clgk1_up_ready));

custom_logic_fork # (.D_WIDTH (D_WIDTH))
CLGC1
(       .clk(clk),
        .rst(rst),
        .up_data(w_fifo1_down_data),
        .up_valid(w_fifo1_down_valid),
        .up_ready(w_clgk1_up_ready),
        .down_data_a(w_clgk1_down_data_a),
        .down_valid_a(w_clgk1_down_valid_a),
        .down_ready_a(w_fifo2_up_ready),
        .down_data_b(w_clgk1_down_data_b),
        .down_valid_b(w_clgk1_down_valid_b),
        .down_ready_b(w_fifo3_up_ready));

ff_fifo_pow2_depth # (.D_WIDTH (D_WIDTH), .A_WIDTH (A_WIDTH))
FIFO2
(       .clk(clk),
        .rst(rst),
        .up_data(w_clgk1_down_data_a),
        .up_valid(w_clgk1_down_valid_a),
        .up_ready(w_fifo2_up_ready),
        .down_data(down_data_a),
        .down_valid(down_valid_a),
        .down_ready(down_ready_a));

ff_fifo_pow2_depth # (.D_WIDTH (D_WIDTH), .A_WIDTH (A_WIDTH))
FIFO3
(       .clk(clk),
        .rst(rst),
        .up_data(w_clgk1_down_data_b),
        .up_valid(w_clgk1_down_valid_b),
        .up_ready(w_fifo3_up_ready),
        .down_data(down_data_b),
        .down_valid(down_valid_b),
        .down_ready(down_ready_b));

endmodule
