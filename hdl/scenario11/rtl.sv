//---TOP MODULE FOR RTL DESIGN---//

module rtl #(parameter D_WIDTH = 6, A_WIDTH = 2)
(
input                   clk,
input                   rst,
input  [(D_WIDTH-1):0]  up_data_a,
input                   up_valid_a,
output                  up_ready_a,
input  [(D_WIDTH-1):0]  up_data_b,
input                   up_valid_b,
output                  up_ready_b,
output [(D_WIDTH-1):0]  down_data,
output                  down_valid,
input                   down_ready
);

wire  [(D_WIDTH-1):0] w_fifo1_down_data_a;
wire                  w_fifo1_down_valid_a;
wire                  w_clgk1_up_ready_a;
wire  [(D_WIDTH-1):0] w_fifo2_down_data_b;
wire                  w_fifo2_down_valid_b;
wire                  w_clgk1_up_ready_b;
wire  [(D_WIDTH-1):0] w_clgk1_down_data;
wire                  w_clgk1_down_valid;
wire                  w_fifo3_up_ready;

ff_fifo_pow2_depth # (.D_WIDTH (D_WIDTH), .A_WIDTH (A_WIDTH))
FIFO1
(       .clk(clk),
        .rst(rst),
        .up_data(up_data_a),
        .up_valid(up_valid_a),
        .up_ready(up_ready_a),
        .down_data(w_fifo1_down_data_a),
        .down_valid(w_fifo1_down_valid_a),
        .down_ready(w_clgk1_up_ready_a));

ff_fifo_pow2_depth # (.D_WIDTH (D_WIDTH), .A_WIDTH (A_WIDTH))
FIFO2
(       .clk(clk),
        .rst(rst),
        .up_data(up_data_b),
        .up_valid(up_valid_b),
        .up_ready(up_ready_b),
        .down_data(w_fifo2_down_data_b),
        .down_valid(w_fifo2_down_valid_b),
        .down_ready(w_clgk1_up_ready_b));

custom_logic_join # (.D_WIDTH (D_WIDTH))
CLGC1
(       .clk(clk),
        .rst(rst),
        .up_data_a(w_fifo1_down_data_a),
        .up_valid_a(w_fifo1_down_valid_a),
        .up_ready_a(w_clgk1_up_ready_a),
        .up_data_b(w_fifo2_down_data_b),
        .up_valid_b(w_fifo2_down_valid_b),
        .up_ready_b(w_clgk1_up_ready_b),
        .down_data(w_clgk1_down_data),
        .down_valid(w_clgk1_down_valid),
        .down_ready(w_fifo3_up_ready));

ff_fifo_pow2_depth # (.D_WIDTH (D_WIDTH), .A_WIDTH (A_WIDTH))
FIFO3
(       .clk(clk),
        .rst(rst),
        .up_data(w_clgk1_down_data),
        .up_valid(w_clgk1_down_valid),
        .up_ready(w_fifo3_up_ready),
        .down_data(down_data),
        .down_valid(down_valid),
        .down_ready(down_ready));

endmodule
