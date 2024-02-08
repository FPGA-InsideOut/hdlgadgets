//---AXI-STREAM FLOP-BASED FIFO WITH CREDIT RETURN UPSTREAM SIGNAL WITH DEPTH OF PWR OF 2---//
//Valid/Rready flags generation is based on comparison of write & read counters
//and their MSBs that indicate "Wrap-around", as per Clifford_E_Cummings.

module ff_fifo_credret_pow2_depth #(parameter D_WIDTH = 6, A_WIDTH = 2)
(
input                   clk,
input                   rst,
input  [(D_WIDTH-1):0]  up_data,
input                   up_valid,
output                  up_ready,
output                  up_credit,
output [(D_WIDTH-1):0]  down_data,
output                  down_valid,
input                   down_ready
);

wire push, pop;
wire empty, full;
wire [(A_WIDTH-1):0] wr_ptr, rd_ptr;

reg [(A_WIDTH):0]   fullwidth_wr_ptr, fullwidth_rd_ptr;
reg [(D_WIDTH-1):0] ram[2**A_WIDTH-1:0];


always @ (posedge clk)
 begin
  if (push)
   ram[wr_ptr] <= up_data;
 end

//WR_COUNTER
always @(posedge clk)
if (rst) begin
 fullwidth_wr_ptr <= {(A_WIDTH+1){1'b0}};
 end else if (push) begin
 fullwidth_wr_ptr <= fullwidth_wr_ptr + 1;
 end

//RD_COUNTER
always @(posedge clk)
if (rst) begin
 fullwidth_rd_ptr <= {(A_WIDTH+1){1'b0}};
 end else if (pop) begin
 fullwidth_rd_ptr <= fullwidth_rd_ptr + 1;
 end

//Generate push and pop signals
assign push = up_valid & up_ready;
assign pop = down_valid & down_ready;

//output LSBits out of full_wr_ptr
assign wr_ptr = fullwidth_wr_ptr[(A_WIDTH-1):0];
//output LSBits out of full_rd_ptr
assign rd_ptr = fullwidth_rd_ptr[(A_WIDTH-1):0];

//"empty"
//It is "1" when MSBits and other bits of "full_rd_ptr" and "full_wr_ptr" are equal
  assign empty = ((fullwidth_wr_ptr[(A_WIDTH)] == fullwidth_rd_ptr[(A_WIDTH)]) &&
                         (fullwidth_wr_ptr[(A_WIDTH-1):0] == fullwidth_rd_ptr[(A_WIDTH-1):0])) ? 1'b1 : 1'b0;
//"valid" aka "not_empty"
  assign down_valid = ~empty;

//"full"
//It is "1" when MSBits of "full_rd_ptr" and "full_wr_ptr" are not equal but other bits equal
  assign full = ((fullwidth_wr_ptr[(A_WIDTH)] != fullwidth_rd_ptr[(A_WIDTH)]) &&
                         (fullwidth_wr_ptr[(A_WIDTH-1):0] == fullwidth_rd_ptr[(A_WIDTH-1):0])) ? 1'b1 : 1'b0;
//"ready" aka "not_full"
  assign up_ready = ~full;

assign down_data = ram[rd_ptr];

//"credit return" when "pop"
  assign up_credit = pop;

endmodule
