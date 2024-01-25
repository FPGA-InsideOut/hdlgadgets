module shiftreg_4depth #(parameter D_WIDTH = 6)
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

reg                     valid0, valid1, valid2, valid3;
reg [(D_WIDTH-1):0]     data0, data1, data2, data3;

//Data
always @(posedge clk)
  if (down_ready) begin
      data0 <= up_data;
      data1 <= data0;
      data2 <= data1;
      data3 <= data2;
  end

//Valid
always @(posedge clk)
if (rst) begin
      valid0 <= 1'b0;
      valid1 <= 1'b0;
      valid2 <= 1'b0;
      valid3 <= 1'b0;
 end else if (down_ready) begin
      valid0 <= up_valid;
      valid1 <= valid0;
      valid2 <= valid1;
      valid3 <= valid2;
 end

assign down_valid = valid3;
assign down_data = data3;
assign up_ready = down_ready;

endmodule
