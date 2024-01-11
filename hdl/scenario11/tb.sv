module tb
# (
  parameter D_WIDTH = 6, A_WIDTH = 2
);

  //--------------------------------------------------------------------------
  // Signals to drive Device Under Test - DUT

  logic                 clk;
  wire                  rst;

  // Upstream

  wire                  up_valid_a;
  wire                  up_ready_a;
  wire [(D_WIDTH-1):0]  up_data_a;

  wire                  up_valid_b;
  wire                  up_ready_b;
  wire [(D_WIDTH-1):0]  up_data_b;

  // Downstream

  wire                  down_valid;
  wire                  down_ready;
  wire [(D_WIDTH-1):0]  down_data;

  // Model

  wire [(D_WIDTH-1):0]  model_data_a;
  wire [(D_WIDTH-1):0]  model_data_b;

  //--------------------------------------------------------------------------
  // DUT instantiation

rtl # (.D_WIDTH (D_WIDTH), .A_WIDTH (A_WIDTH))
RTL1
(       .clk(clk),
        .rst(rst),
        .up_data_a(up_data_a),
        .up_valid_a(up_valid_a),
        .up_ready_a(up_ready_a),
        .up_data_b(up_data_b),
        .up_valid_b(up_valid_b),
        .up_ready_b(up_ready_b),
        .down_data(down_data),
        .down_valid(down_valid),
        .down_ready(down_ready));

  //--------------------------------------------------------------------------
  // MODEL instantiation

wire push_a;
wire push_b;
wire pop_a;
wire pop_b;

assign push_a = up_valid_a & up_ready_a;
assign push_b = up_valid_b & up_ready_b;
assign pop_a = ~down_data[0] & down_valid & down_ready;
assign pop_b = down_data[0] & down_valid & down_ready;

model # (.D_WIDTH (D_WIDTH))
MDL1
(       .clk(clk),
        .rst(rst),
        .up_data_a(up_data_a),
        .up_data_b(up_data_b),
        .push_a(push_a),
        .push_b(push_b),
        .down_data_a(model_data_a),
        .down_data_b(model_data_b),
        .pop_a(pop_a),
        .pop_b(pop_b));

  //--------------------------------------------------------------------------
  // CHECKING modules instantiation

check # (.D_WIDTH (D_WIDTH))
CHK1
(
        .rtl_data(down_data),
        .rtl_valid(down_valid),
        .model_data_a(model_data_a),
        .model_data_b(model_data_b));

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
