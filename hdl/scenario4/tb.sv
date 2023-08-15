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

  wire                  down_valid;
  wire                  down_ready;
  wire [(D_WIDTH-1):0]  down_data;

  //--------------------------------------------------------------------------
  // DUT instantiation

rtl # (.D_WIDTH (D_WIDTH), .A_WIDTH (A_WIDTH))
RTL1
(       .clk(clk),
        .rst(rst),
        .up_data(up_data),
        .up_valid(up_valid),
        .up_ready(up_ready),
        .down_data(down_data),
        .down_valid(down_valid),
        .down_ready(down_ready));

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
