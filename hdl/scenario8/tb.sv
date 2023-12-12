module tb
# (
  parameter D_WIDTH = 6, A_WIDTH = 2
);

  //--------------------------------------------------------------------------
  // Signals to drive Device Under Test - DUT

  logic                 clk;
  wire                  rst;

  // Upstream

  wire                  up_valid;
  wire                  up_ready;
  wire [(D_WIDTH-1):0]  up_data;

  // Downstream

  wire                  down_valid_a;
  wire                  down_ready_a;
  wire [(D_WIDTH-1):0]  down_data_a;

  wire                  down_valid_b;
  wire                  down_ready_b;
  wire [(D_WIDTH-1):0]  down_data_b;

  // Model

  wire [(D_WIDTH-1):0]  model_data_a;
  wire [(D_WIDTH-1):0]  model_data_b;

  //--------------------------------------------------------------------------
  // DUT instantiation

rtl # (.D_WIDTH (D_WIDTH), .A_WIDTH (A_WIDTH))
RTL1
(       .clk(clk),
        .rst(rst),
        .up_data(up_data),
        .up_valid(up_valid),
        .up_ready(up_ready),
        .down_data_a(down_data_a),
        .down_valid_a(down_valid_a),
        .down_ready_a(down_ready_a),
        .down_data_b(down_data_b),
        .down_valid_b(down_valid_b),
        .down_ready_b(down_ready_b));

  //--------------------------------------------------------------------------
  // MODEL instantiation

wire push;
wire pop_a;
wire pop_b;

assign push = up_valid & up_ready;
assign pop_a = down_valid_a & down_ready_a;
assign pop_b = down_valid_b & down_ready_b;

model # (.D_WIDTH (D_WIDTH))
MDL1
(       .clk(clk),
        .rst(rst),
        .up_data(up_data),
        .push(push),
        .down_data_a(model_data_a),
        .down_data_b(model_data_b),
        .pop_a(pop_a),
        .pop_b(pop_b));

  //--------------------------------------------------------------------------
  // CHECKING modules instantiation

check # (.D_WIDTH (D_WIDTH))
CHK1
(
        .rtl_data(down_data_a),
        .rtl_valid(down_valid_a),
        .model_data(model_data_a));

check # (.D_WIDTH (D_WIDTH))
CHK2
(
        .rtl_data(down_data_b),
        .rtl_valid(down_valid_b),
        .model_data(model_data_b));

  //--------------------------------------------------------------------------
  // Driving clock

  initial
  begin
    forever #5 clk = ~ clk;
  end

  //--------------------------------------------------------------------------
  //Initialization and driving simulation
  initial
  begin
    clk = 0;
    forever @ (posedge clk);
  end

endmodule
